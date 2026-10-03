# Contributing

Want to suggest an account for the list? Two ways:

## 1. Open an issue (easiest)

No git needed. Include:

- The account's handle (Threads) or name (Facebook)
- Evidence: a link to or screenshot of the hostile comment
- Which bucket it fits, if you know: `physical_inflection`, `quotation_knights`, `thieves`, `other_hostile`

## 2. Submit a pull request

- Fork the repo
- Add a row to `blocklist.md`: `| handle | Threads |` (or `| Name | Facebook |`)
- Add the entry to `skill/blocklist.json` (`{"threads": "handle"}` or `{"facebook": "Name"}`)
- Open the PR against `master`

## The bar

- The account must have posted something hostile toward AI-assisted musicians — hostility, threats, slurs, harassment. Disagreement with AI, or criticism of the music itself, doesn't qualify.
- One documented incident is enough for the list. Categorization needs a preserved comment.
- The maintainer reviews everything. Nothing merges without his word.
