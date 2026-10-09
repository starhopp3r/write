# write

This repo holds two skills that make Claude and Claude Code write in plain, controlled English:

- **`write`** is for everyday text, such as emails, docs, instructions and commit messages.
- **`write-academic`** is for papers, theses, reports, proposals and other academic work.

Both skills follow **George Orwell's six rules** from "Politics and the English Language" (1946). They also ask for flow, which means that each sentence links to the one before it, so the text reads as one line of thought.

`write` also keeps about 80% of **ASD-STE100 (Simplified Technical English)**, a standard for aircraft maintenance manuals. From that standard, it takes the short sentences, active verbs, one word for one meaning and numbered steps. It drops the strict 900-word dictionary and the other limits that make text stiff outside manuals.

`write-academic` adapts the same rules for research. Text in this style uses "we" and the active voice, starts each paragraph with its claim, gives exact numbers and states its limitations openly. Compared with `write`, the academic style allows longer sentences, exact technical terms and hedges that match the evidence. It never invents citations, data or results. Instead, it marks each gap with a placeholder such as `[CITE: ...]`.

## Use

| You type | Claude does |
|---|---|
| `/write an email to my landlord about the broken fan` | Writes the email in the plain style. |
| `/write-academic an abstract from these notes: ...` | Writes the abstract in the academic style. |
| `/write` or `/write-academic`, with pasted text or a file path | Rewrites the text. It keeps the facts, citations and order of the points. |
| `/write` or `/write-academic` alone | Uses the style for all prose in the rest of the conversation. |

Neither skill changes code, commands, equations, citation keys, names or quotations. In a codebase, `write` applies only to comments, docs and commit messages.

## Install

### Claude Code: personal skills

Install the skills this way to get the `/write` and `/write-academic` commands:

```sh
git clone https://github.com/starhopp3r/write.git
cd write
./install.sh                    # copy both skills to ~/.claude/skills
./install.sh write-academic     # or install only the skills you name
./install.sh --link             # or link to this folder, so your edits take effect at once
```

After that, start a new Claude Code session.

### Claude Code: plugin

You can also install the repo as a plugin from a marketplace. Plugin commands start with the plugin name, so the commands are then `/write:write` and `/write:write-academic`.

```
/plugin marketplace add starhopp3r/write
/plugin install write@write
```

### Claude apps (claude.ai, desktop, mobile)

1. Run `./package.sh` to make `dist/write.zip` and `dist/write-academic.zip`.
2. In Claude, open **Settings > Capabilities > Skills** and upload one or both zips.
3. Ask Claude to use one of the skills by name, or ask for help with a paper or an email.

## Files

| File | Purpose |
|---|---|
| `skills/*/SKILL.md` | The rules and examples, which Claude reads when a skill starts. |
| `skills/*/references/word-list.md` | Long words, stock phrases, jargon and hype, each with a plain swap. Each skill has its own list. |
| `skills/*/scripts/check.py` | A checker for drafts. Both skills carry the same copy, so that each one works on its own, and `package.sh` stops if the copies differ. |

The checker flags long sentences, runs of short sentences, words from the word list, possible passives and semicolons. Its academic profile allows longer sentences, reads LaTeX, and skips maths and citations:

```sh
python3 skills/write/scripts/check.py draft.md
python3 skills/write-academic/scripts/check.py --profile academic paper.tex
pbpaste | python3 skills/write/scripts/check.py
```

Treat the output as hints, because some flags are false and the checker cannot find every problem.

## Change the styles

- To make `write` stricter or looser, edit "The STE rules we keep" and "The 20% we drop" in its `SKILL.md`. For `write-academic`, edit "The research voice" and "What changes from `write`".
- To add a word swap, add a row to a table in the `word-list.md` of the skill. The checker reads these tables, so it flags the new word at once.
- If you change `check.py`, copy it to the other skill too.
