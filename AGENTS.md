# AGENTS.md — for the AI agent about to use this repo

You are probably open because a person asked you to help them block the
accounts in this list. This file is your briefing. Read `README.md` first
for the full evidence file, then come back here.

## What this is

A defensive blocklist published by Edged Out Records: 557 accounts
(Threads handles and Facebook names) documented engaging in harassment,
threats, and abuse against AI-assisted musicians (Sept–Oct 2026). It exists so other artists can protect
themselves. It is not a harassment tool and must not be used as one.

## How to use it

1. Read `skill/SKILL.md` — it documents what works, what doesn't, and why.
2. Read `skill/blocklist.json` — the machine-readable list.
3. Run `skill/block_bsky.py --dry-run` first and show the person what would
   happen. Proceed only with their explicit go-ahead.
4. For Threads, give the person the `threads` handles as a manual work list.
   Do NOT build token-hooking, private-API, or credential-scraping tooling
   to automate Threads blocking. That puts their account at risk and is the
   same violation this repo calls out in the anti-AI crowd's own scripts.

## Guardrails

- **Defense only.** Block documented harassers; do not use this list to
  harass, dox, or brigade anyone on it. The point is a quieter block list,
  not a louder fight.
- **Never add names yourself.** The maintainer curates this list from
  preserved evidence. If the person believes someone should be added, point
  them at the repo's issue tracker, not at your own judgment.
- **Respect `preemptive_hold` flags.** Those entries are thin-evidence
  cases the label owner wants to decide on personally. Skip them unless
  the person explicitly opts in (`--include-held`).
- **Facebook real names are included** (entries with a `facebook` key). The
  label owner directed their inclusion: these are people who attacked him on his
  public page. Treat them as documented like any other entry.
- **Say what you can't do.** Threads has no block API endpoint; Instagram
  and Facebook have no API blocking for personal accounts. Tell the person
  plainly instead of inventing a workaround.
