// 想定型（src/data/archetypes.json）の抜けの確認。警告だけでビルドは止めない（Cloudflare のビルドで使う）。
// 作り直しは週次の scripts/update_type_pool.py（.claude/commands/weekly-pool-update.md）。
import fs from "node:fs";
import path from "node:path";

const read = (f) => JSON.parse(fs.readFileSync(path.join(process.cwd(), f), "utf8"));
const warn = (s) => console.warn(`[archetypes] ${s}`);
try {
  const arch = read("src/data/archetypes.json");
  const seasons = read("src/data/ranking.json").seasons;
  const last = Object.keys(seasons).at(-1);
  const keyOf = {};
  const dir = "src/content/pokemon";
  for (const f of fs.readdirSync(dir).filter((f) => f.endsWith(".md"))) {
    const head = fs.readFileSync(path.join(dir, f), "utf8").split("---")[1] ?? "";
    const get = (k) => head.match(new RegExp(`^${k}:\\s*['"]?([^'"\\n]*)`, "m"))?.[1]?.trim();
    const name = get("pokemonName"), dex = get("dexNumber");
    if (name && dex) keyOf[name] = `${dex.padStart(4, "0")}-${get("imageForm") || "00"}`;
  }
  for (const s of read("public/builder-data/species.json")) keyOf[s.n] ??= s.icon;
  const miss = seasons[last].pokemon.filter((p) => !arch[keyOf[p.name] ?? p.id]).map((p) => p.name);
  if (miss.length) warn(`${last} のランキングにあって想定型が無い ${miss.length}種: ${miss.join("、")}`);
  const old = Object.entries(arch).filter(([k, v]) => !k.startsWith("_") && v.season !== last);
  if (old.length) warn(`想定型のシーズンが最新の ${last} でない ${old.length}種: ${old.map(([k, v]) => `${k}(${v.season})`).join("、")}`);
  const bver = fs.existsSync("public/builder-data/version.json") ? read("public/builder-data/version.json").pool : null;
  const page = fs.existsSync("scripts/pool_versions.json") ? read("scripts/pool_versions.json").page : null;
  if (arch._version !== bver || (page && arch._version !== page)) {
    warn(`版が揃っていない: 想定型 ${arch._version}・1v1(builder-data) ${bver}・pool_versions.json の page ${page}（Set N の番号がずれる）`);
  }
  if (!miss.length && !old.length && arch._version === bver) console.log(`[archetypes] OK ${last}・${arch._version}`);
} catch (e) {
  warn(`確認できませんでした: ${e.message}`);
}
