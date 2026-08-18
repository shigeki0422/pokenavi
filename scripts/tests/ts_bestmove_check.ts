// bestMove(damage.ts)の技選定が「1発目のダメージ最大」ではなく「確定数が最小」であることの回帰検証。
// scripts/tests/test_ts_bestmove.py から esbuild + node で実行される。
import fs from "node:fs";
import path from "node:path";
import { bestMove, calcDamage, simulateKO } from "../../src/scripts/party-builder/damage";
import { bestMoveHitDetail, judge1v1 } from "../../src/scripts/party-builder/matchup";
import { resolveTarget } from "../../src/scripts/party-builder/balance";
import type { MoveDict, ResolvedBuild, TargetGroup } from "../../src/scripts/party-builder/types";

const DATA_DIR = path.join(process.cwd(), "public", "builder-data");
const read = <T,>(rel: string): T => JSON.parse(fs.readFileSync(path.join(DATA_DIR, rel), "utf8"));
const moves = read<MoveDict>("moves.json");
const targets = read<TargetGroup[]>("targets.json");

const builds: { key: string; b: ResolvedBuild }[] = [];
for (const g of targets) {
  for (const b of g.builds) {
    try {
      builds.push({ key: `${g.sp}/${b.label ?? g.sp}`, b: resolveTarget(g.sp, g.label ?? g.sp, g.icon, b, moves) });
    } catch { /* skip */ }
  }
}
const find = (k: string) => builds.find((x) => x.key === k)?.b ?? null;

const results: { name: string; ok: boolean; detail: string }[] = [];
const push = (name: string, ok: boolean, detail = "") => results.push({ name, ok, detail });

// 1) 具体例: メガカイリュー vs ブラッキー。りゅうせいぐん(1発目最大)はC-2で失速し確定5、
//    りゅうのはどう等の非弱化技の方が確定4で早い。選ばれる技の確定数が5未満であること。
{
  const a = find("カイリュー/メガカイリュー");
  const d = find("ブラッキー/ブラッキー");
  if (!a || !d) push("メガカイリュー/ブラッキーのビルドが存在", false, "targets.jsonに見つからない");
  else {
    const best = bestMove(a, d)!;
    const hp = Math.max(1, d.stats[0]);
    const koBest = simulateKO(a, best.move, d, hp, 0, { maxUses: 8 });
    const meteor = (a.pool ?? a.moves).find((m) => m.n === "りゅうせいぐん");
    const koMeteor = meteor ? simulateKO(a, meteor, d, hp, 0, { maxUses: 8 }) : -1;
    push("メガカイリューはブラッキーにりゅうせいぐんを選ばない", best.move.n !== "りゅうせいぐん", `選択=${best.move.n}`);
    push("選択技の確定数がりゅうせいぐんより少ない", koMeteor > 0 && koBest < koMeteor, `best=${koBest} meteor=${koMeteor}`);
    push("りゅうせいぐんは1発目ダメージ最大(前提の確認)",
      calcDamage(a, d, meteor!, { randomRoll: 0 }) > calcDamage(a, d, best.move, { randomRoll: 0 }),
      "");
  }
}

// 2) 全ビルド総当たり: 選ばれた技の確定数が、他のどの候補技の確定数より大きくならない
//    （＝選定基準が確定数最小になっている）。
{
  let bad = 0;
  let sample = "";
  for (const x of builds) {
    for (const y of builds) {
      const best = bestMove(x.b, y.b);
      if (!best) continue;
      const hp = Math.max(1, y.b.stats[0]);
      const koBest = simulateKO(x.b, best.move, y.b, hp, 0, { maxUses: 8 });
      for (const mv of (x.b.pool ?? x.b.moves)) {
        if (mv.cat === "status" || !mv.power) continue;
        const ko = simulateKO(x.b, mv, y.b, hp, 0, { maxUses: 8 });
        if (ko < koBest) {
          bad++;
          if (!sample) sample = `${x.key}→${y.key}: 選択${best.move.n}(${koBest}) より ${mv.n}(${ko})`;
        }
      }
    }
  }
  push("選ばれた技より確定数の少ない候補技が存在しない", bad === 0, `違反=${bad} ${sample}`);
}

// 3) ポップアップの技内訳セル(bestMoveHitDetail)と判定行(judge1v1)の整合。
//    内訳が「確定n」(certain)を出す場合、それは最低乱数での確定数＝判定行のmyHitsと一致しなければ
//    ならない。オボンのみ持ちに対する確率計算が実効HP近似でオボン発動を取りこぼし、
//    「乱数2発」を確率100%＝「確定2」と表示して判定行の「確定3」と矛盾する不具合の回帰テスト。
{
  let bad = 0;
  let sample = "";
  for (const x of builds) {
    for (const y of builds) {
      const d = bestMoveHitDetail(x.b, y.b);
      if (!d || d.hits == null || !d.certain) continue;
      const v = judge1v1(x.b, y.b);
      if (v.myHits !== d.hits) {
        bad++;
        if (!sample) sample = `${x.key}→${y.key}: 内訳確定${d.hits}(${d.n}) vs 判定確定${v.myHits}(${v.myMove})`;
      }
    }
  }
  push("技内訳の「確定n」が判定行の確定数と一致する", bad === 0, `不一致=${bad} ${sample}`);
}

// 4) 具体例: メガカイリュー(ひかえめ) vs オボンのみアシレーヌ。10まんボルトは最低乱数だと
//    オボン回復で確定3、最大乱数なら2発。内訳は「確定2」ではなく乱数表示になること。
{
  const a = builds.find((x) => x.b.item === "カイリュナイト" && x.key.startsWith("カイリュー/"))?.b ?? null;
  const d = builds.find((x) => x.key.startsWith("アシレーヌ/") && x.b.item === "オボンのみ")?.b ?? null;
  if (!a || !d) push("メガカイリュー/オボンアシレーヌのビルドが存在", false, "targets.jsonに見つからない");
  else {
    const det = bestMoveHitDetail(a, d)!;
    const v = judge1v1(a, d);
    push("カイリュー→オボンアシレーヌの内訳が乱数表示(確定ではない)", det.certain === false, `hits=${det.hits} certain=${det.certain} prob=${det.prob}`);
    push("同ケースの判定行は確定3", v.myHits === 3, `myHits=${v.myHits}`);
  }
}

process.stdout.write(JSON.stringify(results));
