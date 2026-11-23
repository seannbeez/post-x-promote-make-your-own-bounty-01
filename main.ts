// Entry program for make.fun bounty "post-x-promote-make-your-own-bounty-01"
// (Node 22, standard library only).
//
// The entry itself is a post on X: one public post that quotes make.fun's
// make-your-own-bounty post (https://x.com/makefunai/status/2124915864336236646)
// or links to it, with a photo of its own attached, make.fun or the @makefunai
// tag and the entrant's play code in its text. POST.json at this repository's
// root names that post's address, and the house reads the post's replies,
// reposts and quotes from X. Places go by replies + reposts + quotes.
//
// All this program has to do is hand POST.json to the gate: it reads the file
// from the repository, checks it is a JSON object carrying a `url` string,
// and writes it unchanged to /output/POST.json. Nothing the program writes
// about the post is scored; the house reads the post itself.
//
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// `out/POST.json` is then byte for byte this directory's POST.json.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const sourcePath = join(BOT_DIR, "POST.json");

// Read first, so a missing or malformed POST.json fails loudly here instead
// of silently handing the gate a broken file.
const raw = readFileSync(sourcePath, "utf8");
const parsed: unknown = JSON.parse(raw);
if (
  typeof parsed !== "object" ||
  parsed === null ||
  Array.isArray(parsed) ||
  typeof (parsed as { url?: unknown }).url !== "string"
) {
  console.error("POST.json must be a JSON object with a string `url` field.");
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
copyFileSync(sourcePath, join(OUTPUT_DIR, "POST.json"));
console.log(`POST.json copied to ${join(OUTPUT_DIR, "POST.json")}`);
