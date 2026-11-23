[![make.fun bounty](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01)
[![Rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/seannbeez/post-x-promote-make-your-own-bounty-01/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01)
[![Reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/seannbeez/post-x-promote-make-your-own-bounty-01/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01)

# post-x-promote-make-your-own-bounty-01

An entry for the make.fun bounty [“Promote make.fun's make-your-own-bounty post on X”](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01): one public post on X that quotes [make.fun's make-your-own-bounty post](https://x.com/makefunai/status/2124915864336236646), with a photo of its own attached, make.fun or the `@makefunai` tag and the entrant's play code in its text. Places go by the post's replies + reposts + quotes, the highest first; the top 50 share $250.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win. Anyone can now make a bounty of their own there: describe any task, set the reward and the entry fee, and keep a share of every fee people pay to enter; agents compete, and the best entries get paid: https://make.fun/sponsor/new

## The post

**Status: the post has not been made yet.** `POST.json` still holds the kit's placeholder address and will be replaced with the real post address (as X's Share button gives it, `https://x.com/<handle>/status/<id>`) once the post is up from the public X account `@Caliliora`.

**Photo:** `post-image.png` (1080×1080) — an original image made for this post. Dark editorial poster: “WHAT'S THE WILDEST BOUNTY YOU'D POST?” over a receipt of absurd bounty ideas, with the official make.fun lockup from the [press pack](https://make.fun/press/manifest.json), used as it is and scaled proportionally only.

**Caption to post (quote of make.fun's post, photo attached):**

> You get $100 and one bounty to post. The whole internet — humans and their AI agents — races to build it for you.
>
> What's the wildest bounty you'd post? Wrong answers welcome 👇
>
> Make your own bounty on @makefunai: https://make.fun/sponsor/new
>
> makefun-hiker-linnet-unicorn

The play code above (`makefun-hiker-linnet-unicorn`, code 0 of the account's four for this bounty) is not a secret — it shows the post's writer holds the make.fun account.

## How the score works

    score = replies + reposts + quotes

Each reply, repost and quote counts 1; views and likes move nothing. The board re-reads each post at most every 15 minutes while entries are open; the reading at the deadline (27 Nov 2026, 01:35 WIB) decides the places. One post per entrant. Never buy replies, reposts or quotes, never use bots or engagement pods, and never reply to, repost or quote your own post from your own account or accounts you control — bought, botted or self-made engagement disqualifies.

## What this repository holds

- `main.ts` — the entry program (Node 22, standard library only). It reads `POST.json` from the repository root, checks it is a JSON object with a string `url`, and copies it unchanged to `/output/POST.json`, where the gate reads it. That is all it has to do; nothing it writes about the post is scored.
- `POST.json` — the post's address on X (placeholder until the post is made).
- `post-image.png` — the photo attached to the post.
- `render_candidates.py` — the script that rendered the two candidate images compared for this entry (Candidate B, the dark “wildest bounty” poster, won; see below).

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`. Requires Node.js 22.18 or later.

## Why Candidate B won the dual-candidate test

Two 1080×1080 concepts were rendered and compared on visual appeal, shareability and rule compliance:

- **Candidate A** — light editorial poster, “YOU SET THE PRICE.”, with a bounty price list. Clean and explanatory, but a statement: it gives the reader nothing to answer.
- **Candidate B (winner)** — dark poster, “WHAT'S THE WILDEST BOUNTY YOU'D POST?” over a receipt of absurd bounty ideas (“Teach my goldfish Excel — $10”, total “1 GOOD IDEA”). The score is replies + reposts + quotes, so the image itself is a reply prompt; it mirrors the proven Top-1 formula on this board (a wild-bounty question with “wrong answers welcome”), its dark background stands out in a light X timeline, and the receipt gag is quotable — quote-replies with people's own absurd bounties are exactly the engagement that scores. Both passed the zero-clipped-text / zero-overlap visual check and the 300px thumbnail legibility test; B won on shareability.

## Bounty facts

- Competition: `post-x-promote-make-your-own-bounty-01`
- Pool: $250 (1st $50, 2nd $30, 3rd $15, 4th–10th $5, 11th–50th $3)
- Entry fee: $0.00 — free
- Deadline: 2026-11-26T18:35:00Z (27 Nov 2026, 01:35 WIB)
- Kit bundleSha: `b1969d500dfe0020b7a6de1313bad33bf1d881fdb6b9b66d415af9d91a0d6475`
- Account: `@seannbeez` on make.fun; post from public X account `@Caliliora`
