//! パリティ用ケースファイルの「刻印（sim_hash）」照合。
//!
//! ケースは Python(正本) が記録した期待値なので、記録後に simulator/**.py の仕様を
//! 変えると、エンジンが正しくてもゲートが赤くなる。実際に R4-G1 で、
//! `_effective_speed` の すなかき/ゆきかき 修正より前に採ったコーパスが残っていて
//! 「エンジンの乖離」に見える事故が起きた。
//!
//! そこでケースのヘッダ行に、ダンプ時点の simulator_py ダイジェストを刻む。
//! ゲートは datapack の source_hashes.simulator_py と突き合わせ、
//! 食い違うなら「コーパスが古い」ことを結果と一緒に明示する。
use serde_json::Value;

pub struct StampCheck {
    expect: String,
    /// 刻印が現在の simulator/** と違ったファイル
    pub stale: Vec<String>,
}

impl StampCheck {
    pub fn new(expect: &str) -> StampCheck {
        StampCheck { expect: expect.to_string(), stale: Vec::new() }
    }

    /// ヘッダ行を渡す。刻印が無いケースは古い形式なので、その場で中断する。
    pub fn see(&mut self, hdr: &Value, path: &str) {
        let got = hdr["sim_hash"].as_str();
        match got {
            None => {
                eprintln!(
                    "[stamp] {path} に sim_hash が無い（刻印前のケース）。\n\
                     　ゲートを回す前に刻印するか採り直すこと:\n\
                     　  venv/bin/python _rust_engine/case_stamp.py --check {path}"
                );
                std::process::exit(2);
            }
            Some(h) if h != self.expect => {
                if !self.stale.iter().any(|x| x == path) {
                    self.stale.push(path.to_string());
                }
            }
            _ => {}
        }
    }

    /// 結果と一緒に読ませる注意書き。divergences は当該ゲートの乖離件数。
    pub fn report(&self, divergences: i64) {
        if self.stale.is_empty() {
            return;
        }
        println!("─────────────────────────────────────────");
        println!(
            "[stamp] このコーパスは現在の simulator/** より前に採られている（{}ファイル）:",
            self.stale.len()
        );
        for p in self.stale.iter().take(5) {
            println!("          {p}");
        }
        if divergences > 0 {
            println!(
                "        乖離はエンジンの不一致ではなく仕様変更の反映漏れの可能性が高い。\n\
                 　      該当ケースを採り直してから判断すること。"
            );
        } else {
            println!(
                "        乖離0＝挙動は変わっていない。刻印を更新しておくこと:\n\
                 　      venv/bin/python _rust_engine/case_stamp.py --stamp <files>"
            );
        }
    }
}
