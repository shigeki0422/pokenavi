// 1v1相性ダイアログの経路が1つ（src/scripts/party-builder/mu-cell-popup.ts）であることの確認。
// ページ側（src/components・src/pages・src/scripts/battle-assist）が表やカードを直接組み立てていたら止める。
import fs from "node:fs";
import path from "node:path";

const roots = ["src/components", "src/pages", "src/scripts/battle-assist"];
const banned = /\b(renderMatchupTable|renderMuPopup|renderMuCard|renderMuTabs|__mtTable)\b|\/matchup_detail\b/;
const hits = [];
const walk = (d) => {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p);
    else if (/\.(astro|ts|js|mjs|tsx)$/.test(e.name)) {
      fs.readFileSync(p, "utf8").split("\n").forEach((line, i) => {
        if (banned.test(line)) hits.push(`${p}:${i + 1}: ${line.trim()}`);
      });
    }
  }
};
roots.filter((r) => fs.existsSync(r)).forEach(walk);
if (hits.length) {
  console.error("[mu-dialog] 1v1相性ダイアログは mu-cell-popup.ts（openMuDialog / renderMuDialog）だけを使ってください:");
  hits.forEach((h) => console.error("  " + h));
  process.exit(1);
}
