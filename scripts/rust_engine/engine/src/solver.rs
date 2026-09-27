//! 終盤の厳密ソルバ（深さ制限つき全幅探索）。
//!
//! MCTS は「現実的な手に絞った部分木」の近似で、どれだけ真の解からずれているかは測れない。
//! ここでは終盤（残りが少ない局面）に限って全幅の木を作り、各ノードを厳密に解く:
//!   - 同時手番ノード: 双方の候補手の利得行列を**混合戦略の均衡**で解いた値（MinMax ではない）
//!   - 偶然ノード: ダメージ乱数を代表点（最低・中間・最高）で列挙した期待値
//!   - 終端: 勝ち=1 / 負け=0、深さ上限では価値ネット
//! 根では各手について「相手の均衡戦略に対する期待勝率」を返すので、AI の選んだ手が
//! 最善からどれだけ損しているか（期待勝率の損失）が測れる。
use crate::battle::{Action, Battle, Side};
use crate::damage::Field;
use crate::net::NetW;
use crate::pack::Pack;
use crate::rng::BRng;
use crate::search::{action_index, candidate_actions, net_eval, NetCtx};
use crate::cpyrng::CpyRandom;
use std::collections::HashMap;

/// ダメージ乱数の代表点（正規化値。0=最低85%・1=最高100%）。一様分布の3点近似。
const ROLLS: [f64; 3] = [0.0, 0.5, 1.0];

pub struct Solver<'a> {
    pub pack: &'a Pack,
    pub net: &'a NetW,
    pub ctx: NetCtx,
    pub collapse_mega: bool,
    pub nodes: u64,
    /// 評価したマス数と、全幅なら評価したはずのマス数（Double Oracle の削減率の計測用）
    pub cells: u64,
    pub cells_full: u64,
    pub double_oracle: bool,
    /// 価値ネットがこの値未満/1-この値超なら決着済みとして展開しない（0で無効＝厳密）
    pub decided: f64,
    /// 命中・急所など内部乱数のサンプル数（ダメージ代表点ごと）
    pub k_samples: u32,
    pub seed_base: i128,
    memo: HashMap<u64, f64>,
}

/// 1ターン進める。roll で乱数を固定し、残りの偶然性（急所・命中など）は seed で決める。
fn step(
    pack: &Pack, sides: &[Side; 2], field: &Field, a1: &Action, a2: &Action, roll: f64, seed: i128,
) -> ([Side; 2], Field, i64) {
    let mut b = Battle { sides: [sides[0].clone(), sides[1].clone()], field: field.clone(), turn: 0, item_snap: Vec::new() };
    b.sides[0].field_idx = 0;
    b.sides[1].field_idx = 1;
    b.field.roll_override = Some(roll);
    let acts = [a1.clone(), a2.clone()];
    let mut rng = CpyRandom::new(seed);
    let w = b.run_loop_lim(pack, &mut rng, 1, |_bt, _r| [acts[0].clone(), acts[1].clone()], |_| {});
    b.field.roll_override = None;
    (b.sides, b.field, w)
}

/// ゼロ和の利得行列（行=自分・最大化）を regret matching+ で解く。
/// 戻り値: (均衡値, 自分の混合戦略, 相手の混合戦略)。
pub fn solve_matrix(a: &[Vec<f64>]) -> (f64, Vec<f64>, Vec<f64>) {
    let m = a.len();
    let n = a[0].len();
    if m == 1 && n == 1 {
        return (a[0][0], vec![1.0], vec![1.0]);
    }
    let (mut rx, mut ry) = (vec![0.0; m], vec![0.0; n]);
    let (mut sx, mut sy) = (vec![0.0; m], vec![0.0; n]);
    let norm = |r: &[f64]| -> Vec<f64> {
        let s: f64 = r.iter().map(|v| v.max(0.0)).sum();
        if s > 0.0 { r.iter().map(|v| v.max(0.0) / s).collect() } else { vec![1.0 / r.len() as f64; r.len()] }
    };
    const T: usize = 3000;
    for t in 1..=T {
        let x = norm(&rx);
        let y = norm(&ry);
        let ux: Vec<f64> = (0..m).map(|i| (0..n).map(|j| a[i][j] * y[j]).sum()).collect();
        let uy: Vec<f64> = (0..n).map(|j| (0..m).map(|i| a[i][j] * x[i]).sum()).collect();
        let vx: f64 = (0..m).map(|i| x[i] * ux[i]).sum();
        let vy: f64 = (0..n).map(|j| y[j] * uy[j]).sum();
        for i in 0..m { rx[i] = (rx[i] + ux[i] - vx).max(0.0); }
        for j in 0..n { ry[j] = (ry[j] - (uy[j] - vy)).max(0.0); }
        let w = t as f64; // 線形重み（RM+ の平均戦略を速く収束させる）
        for i in 0..m { sx[i] += w * x[i]; }
        for j in 0..n { sy[j] += w * y[j]; }
    }
    let zx: f64 = sx.iter().sum();
    let zy: f64 = sy.iter().sum();
    let x: Vec<f64> = sx.iter().map(|v| v / zx).collect();
    let y: Vec<f64> = sy.iter().map(|v| v / zy).collect();
    let v: f64 = (0..m).map(|i| (0..n).map(|j| x[i] * a[i][j] * y[j]).sum::<f64>()).sum();
    (v, x, y)
}

impl<'a> Solver<'a> {
    pub fn new(pack: &'a Pack, net: &'a NetW) -> Self {
        let envf = |k: &str, d: f64| std::env::var(k).ok().and_then(|v| v.parse().ok()).unwrap_or(d);
        Solver {
            pack, net, ctx: NetCtx::new(pack), collapse_mega: true, nodes: 0, cells: 0, cells_full: 0,
            double_oracle: envf("SOLVE_DO", 1.0) > 0.5,
            decided: envf("SOLVE_DECIDED", 0.0),
            k_samples: envf("SOLVE_K", 1.0) as u32,
            seed_base: envf("SOLVE_SEED", 0.0) as i128,
            memo: HashMap::new(),
        }
    }

    fn key(&self, sides: &[Side; 2], field: &Field, me: usize, depth: u32) -> u64 {
        let b = Battle { sides: [sides[0].clone(), sides[1].clone()], field: field.clone(), turn: 0, item_snap: Vec::new() };
        let e = crate::statec::encode_battle(self.pack, &b, false);
        crate::statec::sv_hash(&e.vals) ^ ((me as u64) << 60) ^ ((depth as u64) << 52)
    }

    fn leaf(&mut self, sides: &[Side; 2], field: &Field, me: usize) -> f64 {
        let mut s = [sides[0].clone(), sides[1].clone()];
        let mut f = field.clone();
        let mut rng = CpyRandom::new(1);
        let (_, v1) = net_eval(self.pack, self.net, &mut self.ctx, &mut s, 0, &mut f, &mut rng);
        if me == 0 { v1 } else { 1.0 - v1 }
    }

    /// 1マス（自分の手 am × 相手の手 ao）の期待勝率。ダメージ乱数は代表点で平均する。
    fn cell(&mut self, sides: &[Side; 2], field: &Field, me: usize, depth: u32,
            am: &Action, ao: &Action, i: usize, j: usize) -> f64 {
        let (a1, a2) = if me == 0 { (am, ao) } else { (ao, am) };
        // ダメージ乱数は代表点で列挙するが、命中・急所・追加効果はエンジン内部の乱数で決まる。
        // 1回しか引かないと命中70%の技が「必ず当たる」か「必ず外れる」扱いになり、
        // 値が大きく偏る（その偏った参照解に従って指すと実際には負けた）。K回引いて平均する。
        let mut acc = 0.0;
        let mut cnt = 0.0;
        for (k, &r) in ROLLS.iter().enumerate() {
            for s in 0..self.k_samples {
                let seed = (i as i128) * 1_000_003 + (j as i128) * 10_007 + (k as i128) * 101
                    + (s as i128) * 7_919 + (depth as i128) * 31 + 17 + self.seed_base;
                let (ns, nf, w) = step(self.pack, sides, field, a1, a2, r, seed);
                acc += if w != 0 {
                    if (w == 1) == (me == 0) { 1.0 } else { 0.0 }
                } else {
                    self.value(&ns, &nf, me, depth - 1)
                };
                cnt += 1.0;
            }
        }
        acc / cnt
    }

    /// 局面を解く。戻り値: (均衡値, 自分の各手の「相手の均衡戦略に対する期待勝率」)。
    ///
    /// Double Oracle: 均衡で重みが付く手（サポート）は少ない（実測: 未決着局面で平均1.6手）。
    /// 候補を1手ずつから始めて小さな行列を解き、全候補の中から最善応答を探して足す、を
    /// 双方とも新しい最善応答が出なくなるまで繰り返す。全マスを評価せずに全幅と同じ均衡値になる。
    fn solve(&mut self, sides: &[Side; 2], field: &Field, me: usize, depth: u32)
        -> (f64, Vec<(Action, f64)>)
    {
        let op = 1 - me;
        let mine = candidate_actions(self.pack, &sides[me], &sides[op], field, self.collapse_mega);
        let theirs = candidate_actions(self.pack, &sides[op], &sides[me], field, self.collapse_mega);
        if mine.is_empty() || theirs.is_empty() {
            let v = self.leaf(sides, field, me);
            return (v, mine.into_iter().map(|a| (a, v)).collect());
        }
        let (m, n) = (mine.len(), theirs.len());
        let mut c: Vec<Vec<Option<f64>>> = vec![vec![None; n]; m];
        let mut get = |sv: &mut Self, c: &mut Vec<Vec<Option<f64>>>, i: usize, j: usize| -> f64 {
            if let Some(v) = c[i][j] { return v; }
            let v = sv.cell(sides, field, me, depth, &mine[i], &theirs[j], i, j);
            c[i][j] = Some(v);
            v
        };
        if !self.double_oracle {
            let a: Vec<Vec<f64>> = (0..m).map(|i| (0..n).map(|j| get(self, &mut c, i, j)).collect()).collect();
            let (v, _x, y) = solve_matrix(&a);
            let per = (0..m).map(|i| (mine[i].clone(), (0..n).map(|j| a[i][j] * y[j]).sum())).collect();
            return (v, per);
        }
        let (mut si, mut sj) = (vec![0usize], vec![0usize]);
        const EPS: f64 = 1e-4;
        loop {
            let a: Vec<Vec<f64>> = si.iter().map(|&i| sj.iter().map(|&j| get(self, &mut c, i, j)).collect()).collect();
            let (v, x, y) = solve_matrix(&a);
            // 自分の最善応答（相手の現在の混合戦略に対して）
            let mut br_i = (0usize, f64::NEG_INFINITY);
            for i in 0..m {
                let u: f64 = sj.iter().zip(&y).map(|(&j, &yj)| if yj > 0.0 { yj * get(self, &mut c, i, j) } else { 0.0 }).sum();
                if u > br_i.1 { br_i = (i, u); }
            }
            // 相手の最善応答（自分の現在の混合戦略に対して・相手は最小化）
            let mut br_j = (0usize, f64::INFINITY);
            for j in 0..n {
                let u: f64 = si.iter().zip(&x).map(|(&i, &xi)| if xi > 0.0 { xi * get(self, &mut c, i, j) } else { 0.0 }).sum();
                if u < br_j.1 { br_j = (j, u); }
            }
            let mut grew = false;
            if br_i.1 > v + EPS && !si.contains(&br_i.0) { si.push(br_i.0); grew = true; }
            if br_j.1 < v - EPS && !sj.contains(&br_j.0) { sj.push(br_j.0); grew = true; }
            if !grew {
                let per = (0..m).map(|i| {
                    let u: f64 = sj.iter().zip(&y).map(|(&j, &yj)| if yj > 0.0 { yj * get(self, &mut c, i, j) } else { 0.0 }).sum();
                    (mine[i].clone(), u)
                }).collect();
                self.cells += c.iter().flatten().filter(|v| v.is_some()).count() as u64;
                self.cells_full += (m * n) as u64;
                return (v, per);
            }
        }
    }

    /// 局面の均衡値（自分 me 視点の勝率）。
    pub fn value(&mut self, sides: &[Side; 2], field: &Field, me: usize, depth: u32) -> f64 {
        self.nodes += 1;
        if !sides[0].has_alive() { return if me == 1 { 1.0 } else { 0.0 }; }
        if !sides[1].has_alive() { return if me == 0 { 1.0 } else { 0.0 }; }
        if depth == 0 {
            return self.leaf(sides, field, me);
        }
        let k = self.key(sides, field, me, depth);
        if let Some(&v) = self.memo.get(&k) {
            return v;
        }
        // 決着がほぼ見えている局面は展開しない（実測で終盤の8割がこれ。どの手でも値が変わらない）
        if self.decided > 0.0 {
            let l = self.leaf(sides, field, me);
            if l < self.decided || l > 1.0 - self.decided {
                self.memo.insert(k, l);
                return l;
            }
        }
        let v = self.solve(sides, field, me, depth).0;
        self.memo.insert(k, v);
        v
    }

    /// 根の解析: (均衡値, [(自分の手index, 相手の均衡戦略に対する期待勝率)])。
    pub fn root(&mut self, sides: &[Side; 2], field: &Field, me: usize, depth: u32)
        -> (f64, Vec<(usize, f64)>)
    {
        let (v, per) = self.solve(sides, field, me, depth);
        (v, per.iter().map(|(a, u)| (action_index(a), *u)).collect())
    }
}

#[cfg(test)]
mod tests {
    use super::solve_matrix;

    #[test]
    fn じゃんけんは均衡値0_5で各手1_3() {
        // 勝=1, 引分=0.5, 負=0（行=自分）
        let a = vec![vec![0.5, 0.0, 1.0], vec![1.0, 0.5, 0.0], vec![0.0, 1.0, 0.5]];
        let (v, x, y) = solve_matrix(&a);
        assert!((v - 0.5).abs() < 1e-3, "v={v}");
        for p in x.iter().chain(y.iter()) {
            assert!((p - 1.0 / 3.0).abs() < 0.02, "x={x:?} y={y:?}");
        }
    }

    #[test]
    fn 支配戦略がある行列は純粋戦略になる() {
        // 行0が常に行1より良い
        let a = vec![vec![0.9, 0.7], vec![0.3, 0.1]];
        let (v, x, _y) = solve_matrix(&a);
        assert!(x[0] > 0.99, "x={x:?}");
        assert!((v - 0.7).abs() < 1e-3, "v={v}");
    }

    #[test]
    fn 同時手番の読み合いは混合戦略になる() {
        // マッチングペニー型: 相手と同じ手なら勝ち
        let a = vec![vec![1.0, 0.0], vec![0.0, 1.0]];
        let (v, x, y) = solve_matrix(&a);
        assert!((v - 0.5).abs() < 1e-3 && (x[0] - 0.5).abs() < 0.02 && (y[0] - 0.5).abs() < 0.02);
    }
}
