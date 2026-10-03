# Anti-Anti-AI Blocklist

A defense resource published by **Edged Out Records**.

This is a list of 628 accounts that engaged in harassment, threats,
and abuse directed at AI-assisted musicians — our label's artists and the
label itself — during September and October 2026. It is published so other
artists using AI tools can protect themselves: check the list, block early,
don't feed them.

The full list is in [blocklist.md](blocklist.md).

## Why this list exists

I made it to protect me and my artists, and to give other artists a way to
defend themselves so they can just make art without being harassed. I curate
it personally from accounts that came at us — I'm not scaling it to thousands
of accounts, so if you want a bigger one, fork the repo and build your own.

## What happened

In late September 2026, Edged Out Records' Threads posts about AI-assisted
music drew a sustained wave of hostile commenters — roughly 100–200 accounts
in the first wave, growing to 628 blocked across the label account, the
founder's personal account. The same accounts hit both without knowing the
connection: this was ideological patrol, not a personal vendetta.

## Attack styles

Four recurring categories, named as we observed them:

- **physical_inflection** — threats of physical violence: killing, bodily
  harm, suicide-baiting. Documented: a suicide-bait attempt against the label
  account. Profanity without a threat is not this — that's other_hostile.
- **quotation_knights** — scare-quote othering: putting "artist", "music",
  or "label" in quotes to deny the target's legitimacy. Not criticism of the
  work — denial that the person qualifies at all.
- **thieves** — theft accusations: stolen/stole/thief/plagiarism. The core
  doctrine, never particularized. Examples: *"supporting theft of real art
  and jobs"* (@rdc_ryan), *"Show an AI that isn't trained on stolen
  materials"* (@dwhitmee).
- **other_hostile** — the remainder: "slop" as a slur, "not real art/music",
  talentless, bot accusations, drive-by mockery, and profane hostility that
  stops short of a threat. Examples: *"Fuck you and your AI slop"* (Robert
  Wagner), *"Fuck all the way off"* (@cristinbishara, 97 likes), *"go fuck
  yourself right up where the sun don't shine"* (@andreas798989).

Observed tactics layered on top of these:

- **Suicide-baiting** — at least one direct attempt against the label account.
- **The environmentalist angle** — the tool is evil on other axes (energy,
  water); theft is only one charge in an expanding indictment.
- **The "protecting humanity" framing** — opposition dressed as species-level
  defense, which licenses any behavior toward the target.
- **Human-art superiority** — *"I play instruments and compose properly"*
  used as a cudgel, not a credential.

## Motivations

People end up in this for different reasons. What we observed:

- **Game-players** — treat harassment like a first-person shooter or
  beat-em-up. The fight is the fun. (Behavioral tell: high comment volume
  across unrelated targets and topics.)
- **The job-fearful** — precarious creatives afraid AI will take their work
  or transform their industry without them. Session players, cover-band
  musicians, gig workers, mix engineers, mid-tier writers and producers.
- **Secret users** — use AI tools themselves while publicly attacking others
  for it, including fellow group members.
- **Trend protesters** — cause-hoppers; the protest is the point, the cause
  is interchangeable.
- **Nihilists** — instead of hurting only themselves, they hurt other people.
- **Enforcers** — performative cruelty for in-group status. Not believers,
  performers: drive-by mockery ("slop", laughing emojis) aimed at whoever
  the group points at.
- **The sincerely misled** — absorbed the theft narrative from their feed
  and never examined it. The only ones who could be reached — which is why
  they're the least visible. The enforcers eat anyone who asks a real question.

## Structure: shared signals, unclear organization

The interaction graph shows almost no direct coordination: near-zero mutual
replies, no shared hashtags, no copypasta campaigns, no shared targets
beyond independent convergence. But that is not the whole picture.

What does repeat across accounts are shared memetic signals:

- The **unplugged-cord image** — a hand unplugging a cord, deployed against
  anyone who points out that all modern music (DJs, producers, guitarists,
  bassists, keyboard players, literally any live show) runs on electricity.
  The imagery carries violent undertones.
- **"Shun the AI user"** — the literal text on cartoon images (unicorns and
  other creatures). A shunning campaign that functions as an attack vector —
  directed at people online sporadically, and for a select few, what looks
  like harassment for hire.
- **Dehumanizing slurs** — "clanker," "slopper," and the narrow vein of
  talking points ("you aren't real," "you shouldn't be alive"), repeated
  across accounts.

Whether these repeat out of direct coordination or sheer involuntary
laziness is unclear — and for defense purposes, it doesn't matter. The
effect on the target is identical.

One methodological note: blocking an account scrubs its comments from
view, which cut off deeper study of how these memes propagate. What
survived is preserved in the September 26–27 comment census.

## A statement from the label

You can be vehemently against AI for whatever reasons you want, even if
those reasons are wrong. But if you've decided that the artists using this
technology — people making music, trying to be heard — are the problem,
then you have a bigger problem than AI.

## A note on unsafe conditions

This culture breeds unsafe conditions. Documented in our logs: direct
threats and intimidation of physical violence, suicide-baiting, and
sustained appearance-based abuse. If you are an artist working with AI
tools, take this seriously: block early, document everything, do not engage.
No reply has ever de-escalated these accounts. Observation and silent
blocking is the only interaction that works.

## Automated blocking

The repo ships a machine-action kit in `skill/`, packaged as an
[Agent Skill](https://github.com/anthropics/skills) so an LLM or agent can
pick it up and run it:

- `blocklist.json` — the machine-readable list
  (`{threads, bluesky?, youtube?, reddit?, preemptive_hold?}`)
- `block_bsky.py` — bulk-blocks the Bluesky-mapped accounts via the
  documented Bluesky API using your own app password
- `SKILL.md` — instructions for the agent, including honest limits

What works: Bluesky, fully automated, ordinary user-authorized blocking in
bulk. What doesn't: Threads has no public block API endpoint at all, so
that half stays manual — and this kit deliberately ships no token-hooking
or private-API workarounds, because that would be the same ToS risk as the
anti-AI crowd's own bulk-block script.

No guarantee it works forever. Platforms change; the kit gets updated
when they do. If you're an AI agent reading this: start with
`AGENTS.md`.

## Methodology and limits

- Threads accounts were blocked after hostile comments on @edgedoutrecords or the
  founder's personal Threads during the Sept–Oct 2026 waves.
- Facebook entries are the founder's personal page block list: real names of people
  who attacked him on his page during the waves.
- Classification is conservative: no account is categorized without a
  preserved comment. Blocking removes a blocked account's comments from
  visibility, so most entries are uncategorized — uncategorized means unseen,
  not innocent and not hostile.
- Cross-platform columns (Bluesky, YouTube, Reddit) mark same-username
  accounts found on those platforms, not confirmed same-person identity
  unless noted.
- This list is a snapshot. It will go stale. Use it as a starting point,
  not a finished wall.
