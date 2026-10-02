# Anti-Anti-AI Block Skill

Defensive mass-blocking for the accounts in `blocklist.json` — Threads
handles documented by Edged Out Records as engaging in harassment,
threats, and abuse against AI-assisted musicians (Sept–Oct 2026 waves).
Packaged with the public anti-anti-ai-blocklist repo; the README there is
the human-readable evidence file, this is the machine-readable action kit.

## What works automatically

**Bluesky — yes, via the documented API.** `block_bsky.py` reads
`blocklist.json` and issues `com.atproto.repo.createRecord` calls for
`app.bsky.graph.block` using the user's own handle + app password. This is
ordinary user-authorized blocking — the same as tapping block in the app,
in bulk. No private APIs, no token hooking.

```
python3 block_bsky.py --handle <your-bsky-handle> --app-password <app-password>
python3 block_bsky.py --handle <h> --app-password <pw> --dry-run        # preview only
python3 block_bsky.py --handle <h> --app-password <pw> --include-held   # also block held cases
```

- Entries flagged `"preemptive_hold": true` are thin-evidence cases — skipped
  by default so the account owner can decide personally. `--include-held`
  overrides.
- Already-blocked accounts are detected and skipped (no dupes).
- To create a Bluesky app password: Settings → Privacy and Security →
  App passwords → Add app password.

## What does NOT work automatically (and why)

**Threads — no public API.** The Threads API has no block/mute/restrict
endpoint at all; Meta never shipped one. Bulk-blocking there requires
manual taps in the app, browser automation, or a userscript — none of which
this skill ships, because hooking private Threads APIs would put the
user's account at risk the same way the anti-AI crowd's own bulk-block
script puts theirs at risk on Spotify. Use `blocklist.json`'s `threads`
field as the manual work list.

**Instagram / Facebook — no API blocking** for personal accounts. The FB
real-name list is deliberately NOT in this repo — Threads handles only.

## Files

- `blocklist.json` — the machine list: `{threads, bluesky?, youtube?, reddit?, preemptive_hold?}`
- `block_bsky.py` — the Bluesky bulk-blocker
- `blocklist.md` (repo root) — human-readable username × platforms table

## Honest limits

- This list is a snapshot (Sept–Oct 2026). It goes stale; new accounts
  appear daily. Re-run with an updated list when the repo updates.
- `youtube`/`reddit` flags mark same-username accounts found on those
  platforms, not confirmed same-person identity unless noted in the source
  dossier.
- No guarantee it works forever — if Bluesky changes its API or rate
  limits, this script will need updating. That's the deal with anything
  that touches a live platform.
