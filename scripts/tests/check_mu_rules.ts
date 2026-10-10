// 1v1判定の入力の規則（test_all.py 47 が呼ぶ）。出力 {名前: [ok, 詳細]}。
// 実行: npx tsx scripts/tests/check_mu_rules.ts
import fs from "node:fs";
import path from "node:path";
import { analyze, buildToSpec, initEngineFrom } from "../../src/scripts/engine/wasm";
import { resolveSlot, resolveTarget } from "../../src/scripts/party-builder/balance";
import { judge1v1, moveDamages } from "../../src/scripts/party-builder/matchup";
import { fromSuggestSpec } from "../../src/scripts/party-builder/spec";
import type { MoveDict, SpeciesMaster, TargetBuild } from "../../src/scripts/party-builder/types";

const ROOT = "/Users/shigeki/work/pokenavi";
const DATA = path.join(ROOT, "public", "builder-data");
const rj = <T,>(f: string): T => JSON.parse(fs.readFileSync(path.join(DATA, f), "utf8"));
await initEngineFrom(fs.readFileSync(process.env.WASM ?? path.join(ROOT, "public", "engine", "engine_wasm.wasm")),
  fs.readFileSync(path.join(DATA, "engine.pack.json"), "utf8"));
const species = rj<SpeciesMaster[]>("species.json");
const moves = rj<MoveDict>("moves.json");
const out: Record<string, [boolean, string]> = {};
const slot = (s: string) => resolveSlot(fromSuggestSpec(s)!, species, moves);
const entry = (a: string, b: string) => {
  const ev = (analyze(a, b).verdict as unknown as { raceInit: { events: { phase: string; side: number; ability: string; effect: boolean }[] } })
    .raceInit.events.find((e) => e.phase === "entry" && e.side === 0);
  return ev ? `${ev.ability}${ev.effect ? "!" : ""}` : "";
};
const GARCHOMP = "ガブリアス@きあいのタスキ:いじっぱり:じしん|つるぎのまい|ほのおのキバ|スケイルショット:2/32/0/0/0/32:さめはだ";

const sala = slot("ボーマンダ@ボーマンダナイト:いじっぱり:げきりん|じしん|すてみタックル|りゅうのまい:2/32/0/0/0/32:いかく");
const salaSpec = buildToSpec(sala);
out["メガ石持ちの自分はメガ前の特性の spec（いかく）・メガ後の特性は megaAbility"] =
  [salaSpec.endsWith(":いかく") && sala.megaAbility === "スカイスキン", `${salaSpec} / ${sala.megaAbility}`];
out["メガ石持ちの自分が いかく で入場して発動する"] = [entry(salaSpec, GARCHOMP) === "いかく!", entry(salaSpec, GARCHOMP)];
const moxie = buildToSpec(slot("ボーマンダ@ボーマンダナイト:いじっぱり:げきりん|じしん|すてみタックル|りゅうのまい:2/32/0/0/0/32:じしんかじょう"));
const oppAtk = (a: string, b: string) => (analyze(a, b).verdict as unknown as { raceInit: { sides: { stg: number[] }[] } }).raceInit.sides[1].stg[0];
out["選んだメガ前の特性（じしんかじょう）で入場する（メガ後の特性に置き換えて元の種族の最多＝いかく にならない）"] =
  [moxie.endsWith(":じしんかじょう") && entry(moxie, GARCHOMP) === "" && oppAtk(moxie, GARCHOMP) === 0 && oppAtk(salaSpec, GARCHOMP) === -1,
   `${moxie.split(":").pop()} entry=${entry(moxie, GARCHOMP)} 相手の攻撃 ${oppAtk(moxie, GARCHOMP)}（いかく ${oppAtk(salaSpec, GARCHOMP)}）`];

const dnite = slot("カイリュー@たべのこし:いじっぱり:じしん|はねやすめ|りゅうのまい|ドラゴンテール:32/2/24/0/0/8:マルチスケイル");
const corvB: TargetBuild = {
  idx: 1, item: "ゴツゴツメット", nature: "わんぱく", ability: "プレッシャー", ev: [32, 0, 32, 0, 2, 0],
  moves: ["てっぺき", "とんぼがえり", "はねやすめ", "ボディプレス"], t1: "ひこう", t2: "はがね", bs: [98, 87, 105, 53, 85, 67], spec: "",
};
const corv = resolveTarget("アーマーガア", "アーマーガア", "0823-00", corvB, moves);
const full = analyze(buildToSpec(dnite), buildToSpec(corv)).verdict.score;
const v = judge1v1(dnite, corv);
out["0倍の技（じしん vs アーマーガア）を含む型の判定がエンジンに全技を渡した結果と同じ（技の前処理に依存しない）"] =
  [v.score === full, `judge1v1 ${v.score} / engine ${full}`];
out["0倍の技を「何もしない手」にしない（じしん で ゴツゴツメット を避けて引き分けにしない。最大打点技も じしん にしない）"] =
  [v.sym === "×" && v.myMove !== "じしん" && !(v.mySeq ?? []).includes("じしん"), `${v.sym} ${v.score} ${v.myMove} ${(v.mySeq ?? []).join(",")}`];
const greninja = "ゲッコウガ@こだわりスカーフ:おくびょう:あくのはどう|みずしゅりけん|れいとうビーム|ヘドロウェーブ:2/0/0/32/0/32:へんげんじざい";
const gallade = "エルレイド@きあいのタスキ:いじっぱり:サイコカッター|せいなるつるぎ|インファイト|かげうち:2/32/0/0/0/32:きれあじ";
const vg = analyze(gallade, greninja).verdict as unknown as { race: { actor: number | null; move: string | null }[] };
out["相手のタイプが試合中に変わって当たるようになった技は撃つ（へんげんじざいで どく になったゲッコウガに サイコカッター）"] =
  [vg.race.some((e) => e.actor === 0 && e.move === "サイコカッター"), JSON.stringify(vg.race.filter((e) => e.actor === 0).map((e) => e.move))];

const salaT: TargetBuild = {
  idx: 1, item: "ボーマンダナイト", nature: "いじっぱり", ability: "いかく", mab: "スカイスキン", ev: [2, 32, 0, 0, 0, 32],
  moves: ["げきりん", "じしん", "すてみタックル", "りゅうのまい"], t1: "ドラゴン", t2: "ひこう", bs: [95, 145, 130, 120, 90, 120], spec: "", mega: true,
};
const megaSala = resolveTarget("ボーマンダ", "ボーマンダ", "0373-00", salaT, moves);
const gengar = slot("ゲンガー@きあいのタスキ:おくびょう:シャドーボール|ヘドロばくだん|10まんボルト|まもる:2/0/0/32/0/32:のろわれボディ");
const dd = moveDamages(gengar, megaSala).opp.find((m) => m.n === "すてみタックル");
out["メガ後の スカイスキン で当たる すてみタックル をゴーストへの計算から外さない（メガ前の特性が いかく の型）"] =
  [!!dd && dd.dmgHi > 0, JSON.stringify(dd ?? null)];

const meow = fromSuggestSpec("ニャオニクス(メス)@ニャオニクスナイト:おくびょう:サイコキネシス|みわくのボイス|10まんボルト|わるだくみ:2/0/0/32/0/32:かちき")!;
out["簡単構築の ニャオニクス(メス) は(メス)のまま・かちき のまま取り込む"] = [meow.sp === "ニャオニクス(メス)" && meow.ability === "かちき", `${meow.sp} ${meow.ability}`];

console.log(JSON.stringify(out));
