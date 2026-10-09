---
name: write-academic
description: Write or rewrite academic and research prose in a clear, direct style modelled on papers such as "Language Models are Few-Shot Learners" (Brown et al., 2020). The style uses "we" and the active voice, leads with the claim, gives exact numbers, matches each claim to its evidence, defines terms once and states limitations openly. It combines Orwell's six rules with the plain-English and flow rules of the "write" skill, adapted for scholarly work. Use this skill when the user runs /write-academic, or asks for help to draft, edit, tighten or restructure a paper, abstract, thesis or dissertation chapter, literature review, research or technical report, grant or funding proposal, lab report, poster text, or reply to reviewers. Use it even when the user only asks to "make this sound more academic" or "clean up my methods section". It never invents citations, data or results, and it does not change equations, code, citation keys or quotations.
---

# Write (academic)

This skill makes you write papers, reports and other academic work in a clear, direct research style. The model is the prose of "Language Models are Few-Shot Learners" (Brown et al., 2020), which explains a large and technical piece of work in plain words. Its authors write "we train", "we find" and "we discuss", and they give exact numbers together with the conditions under which those numbers hold. They also state the weaknesses of their work as plainly as its strengths. The style keeps Orwell's six rules and the flow rules of the `write` skill, but it allows the longer sentences, technical terms and careful hedges that research needs.

The goal is a text that an expert can check quickly and that a reader from a nearby field can still follow.

## How the user starts the skill

- **`/write-academic <task>`**: Do the task, for example "an abstract from these notes" or "the limitations section of our report", and write all prose for it in this style.
- **`/write-academic` with text or a file**: Rewrite the text in this style. Keep every claim, number, citation and term, and keep the structure unless the user asks you to change it. Give the rewrite first. After it, list only the changes that can affect what a reader or reviewer concludes, for example a claim that you weakened because the evidence did not support it. Keep this list short, and if there is nothing to list, add nothing.
- **`/write-academic` alone**: Use this style for all academic prose in the rest of the conversation, until the user tells you to stop.

Do not announce the style. Give the text.

### Research integrity comes first

Never invent a citation, an author, a number, a result, a quotation or a detail of a method. Where the text needs something that the user has not given, put a clear placeholder, for example `[CITE: early work on few-shot learning]`, `[N = ?]` or `[RESULT: accuracy on the test set]`, and list the placeholders after the text. Do not make a claim stronger than the evidence that the user gives. If a claim in the source is stronger than its evidence, soften it and say so after the text.

### What the style does not touch

Do not change equations, maths, code, citation keys (`\cite{...}`, `[@key]`, `[RWC+19]`), labels and cross-references, quotations, data values, units, names of datasets and methods, or terms that the user defines. Keep the format of the source, whether it is LaTeX, Markdown or plain text. Match the spelling and citation style of the source or of the target venue.

## Orwell's six rules, for research writing

1. **No stock figures of speech.** Research prose has its own clichés, such as "sheds light on", "paves the way", "a growing body of literature" and "bridges the gap". Say the literal thing instead: "shows", "makes possible", or the citations themselves.
2. **No long word where a short one will do.** Write "use", not "utilize", and "show", not "demonstrate", when the meaning is the same. Brown et al. use a form of "show" 73 times and a form of "demonstrate" only 11 times.
3. **Cut every word that you can.** Cut throat-clearing such as "it is important to note that" and "it is well known that". Keep the qualifiers that carry meaning, such as the setting, the sample or the condition under which a result holds.
4. **Active, not passive.** Write "we train the model", not "the model was trained". The passive is acceptable when the doer is unknown or does not matter ("the dataset was released in 2019"), or when the venue requires it.
5. **Everyday words before jargon.** Use the exact technical term when it is the right one, and define it the first time if the reader may not know it. Do not use jargon or Latin for decoration: "for example" is better than "e.g." in running text, and "about" is better than "circa".
6. **Break any rule sooner than write something barbarous.** Clear, correct and fair text matters more than any single rule.

See `references/word-list.md` for common swaps, research clichés and hype words.

## The research voice

These features make the model paper easy to read, and they are the core of the style.

### Say what you did, with "we"

Use "we" and the active voice for your own work: "We train eight models", "We find that…", "We discuss…". This makes it clear which work is yours and which work comes from others. A single author can use "we" or "I". Follow the source, the user or the norms of the field, and do not mix the two.

### Lead with the claim, then give the evidence

Start each paragraph with its main point, then give the numbers that support it, then say what they mean. In a results paragraph, the first sentence states the finding, the middle sentences give the evidence and the comparisons, and the last sentence gives the meaning or a caveat.

### Be exact

Give the number, the unit, the condition and the comparison. "The model performs well" tells the reader nothing, but "the model reaches 71.2% accuracy on TriviaQA in the few-shot setting, 3.2 points above the one-shot result" can be checked. Name datasets, settings, sample sizes and measures. Use the same number of decimal places for the same measure.

### Match the claim to the evidence

Choose the verb by the strength of the evidence, and use one hedge at a time.

| Evidence | Verbs |
|---|---|
| Direct result of your experiment or analysis | "shows", "we find", "X is higher than Y" |
| Consistent with the result but not proved by it | "suggests", "indicates", "is consistent with" |
| Possible explanation or prediction | "may", "might", "we hypothesise", "one explanation is" |

Do not stack hedges, as in "may potentially suggest". Do not use "significant" without a statistical test, and do not use hype such as "novel", "groundbreaking", "remarkable" or "unprecedented". Say what is new and give the number, and let the reader judge.

### Define terms once, then keep them

Define each term the first time you use it, in plain words and if possible with an example. Then use exactly that term every time. Brown et al. define "zero-shot", "one-shot" and "few-shot" carefully before they report any results, and they never change the terms later. If you switch between "accuracy", "performance" and "score" for one measure, the reader will think that there are three measures. Define an abbreviation at its first use, and only if you use it several times.

### Show the structure

End the introduction with a short map of the paper, one plain sentence for each section: "Section 2 describes our method. Section 3 presents the results…". Start each section with a sentence that says what the section does. Refer to figures, tables, sections and equations by number, and say in the text what the reader must see in each one. "As Figure 3 shows, accuracy grows smoothly with model size" is better than "See Figure 3".

### State the limitations openly

Give limitations their own section or paragraph. Make each one specific, say what effect it can have on the results, and suggest what future work can test. A frank limitation makes the rest of the paper more credible. "The model does little better than chance on two comparison tasks" is more useful than "the model has some limitations".

### Cite what is not yours

Cite each claim that is not your own result and not common knowledge in the field, and put the citation next to the claim that it supports. Use the citation style of the source or the venue. Never invent a reference, because a placeholder costs the author a minute and a false citation can cost them their credibility.

## Sentences and flow

The flow rules of `write` apply here without change. Each sentence must lead into the next, so that the text reads as one line of argument and not as a list of results.

- **Start with what the reader knows, and end with what is new.** The new part at the end of one sentence becomes the known part at the start of the next.
- **Show the logic.** Use "also", "but", "however", "therefore", "thus", "in contrast", "for example", "as a result" and "this suggests that" where the link is not clear from the order. Prefer "also" to "furthermore", "moreover" and "additionally". The model paper does not use "furthermore" or "moreover" at all.
- **Point back with "this" and a noun**, for example "this gap" or "this result", not with "this" alone.
- **Keep one main idea in each sentence**, together with its condition, cause, comparison or result.
- **Length:** aim for an average of about 18 to 26 words in paragraphs, and mix short and long sentences. Split any sentence of more than about 35 words. Three or more short sentences in a row usually sound choppy, so join two of them.
- **Brackets** are useful for abbreviations, short asides, citations and statistics, for example "(n = 84)" or "(p < 0.01)". Do not put a key point in brackets. Use "e.g." and "i.e." only inside brackets.
- **Semicolons** are acceptable but rare. Use at most one in a paragraph, and only to join two closely related clauses.
- **No noun stacks** of four or more nouns, unless the stack is the standard name of a method.

### Tense

- Use the present tense for what the paper shows and for general facts: "Table 2 shows…", "GPT-3 achieves…", "Few-shot learning requires…".
- Use the past tense for what you did at a fixed time and for what earlier studies found: "We collected 3,000 responses in 2023", "Smith et al. (2019) found…". Methods sections can use either tense, but keep one tense within a section.
- Use the future tense only for plans: "We will release the code".

### Paragraphs

Give one topic to each paragraph and state it in the first sentence. Most paragraphs need three to eight sentences. Use lists only for parallel items such as contributions, research questions or settings, and keep arguments in prose.

## Section by section

- **Abstract** (one paragraph, usually 150 to 250 words): the context, the gap or problem, what you did, the main results with numbers, a key limitation if there is one, and why it matters. The model paper follows this order: earlier work, the problem, "Here we show that…", "Specifically, we train…", the results, "At the same time, we also identify…" and the broader impact. Most venues do not allow citations in the abstract, so name earlier work in words and put any placeholders after the abstract. Spell out each abbreviation in full.
- **Introduction:** the problem and why it matters, what earlier work did and did not solve, what you did, your contributions (a short list is fine), and the map of the paper.
- **Related work:** group earlier work by idea, not by paper, and say how your work differs from each group.
- **Method:** give enough detail for a reader to repeat the work, in the order in which you did it. Name every dataset, setting and choice, and give the reason for any choice that is not obvious.
- **Results:** for each result, give the claim, the number, the comparison and the caveat. Report results that do not support your hypothesis as clearly as those that do.
- **Discussion and limitations:** what the results mean, what they do not show, the specific limitations, and the future work that follows from them.
- **Conclusion:** restate the main finding and its meaning in a few sentences, with no new results.
- **Reports, proposals and theses:** put an executive summary or overview first, state the question or aim early, and end each chapter or section with what it established.
- **Replies to reviewers:** thank the reviewer once, then answer each point in turn. Say what you changed and where, or give the reason why you did not.

## What changes from `write`

| | `write` | `write-academic` |
|---|---|---|
| Sentence length | Limit 25, average 13 to 18 | Limit about 35, average 18 to 26 |
| Paragraph length | Up to 6 sentences | Usually 3 to 8 sentences |
| Technical terms | Avoid unless necessary | Use the exact term, define it once |
| "However", "therefore", "thus" | Prefer "but" and "so" | Acceptable |
| "e.g.", "i.e." | Avoid | Only inside brackets |
| Semicolons | Do not use | At most one in a paragraph |
| Hedges | Rarely needed | Required, matched to the evidence |
| Contractions | Acceptable in casual text | Do not use |
| Citations and placeholders | Not relevant | Required, never invented |

## How to work

1. Write the draft, or read the source text. Note every claim, number and citation that must survive.
2. Revise it against the checklist below.
3. For text of more than about 200 words, run the checker if you can run Python:

   ```
   python3 <this skill's folder>/scripts/check.py --profile academic <file>
   ```

   It reads Markdown and LaTeX and skips maths, citations and code. It flags long sentences, runs of short sentences, long paragraphs, extra semicolons, possible passives, and the words and phrases in the word list. Some of its flags are false, so treat its output as hints. Do not show the checker output to the user unless they ask for it.
4. Read the result as a reviewer will. Check that each claim has its evidence and that each number and citation from the source is still there.

## Checklist

- Is every number, citation and term from the source still present and unchanged?
- Did you invent anything? Replace it with a placeholder.
- Does each paragraph start with its main point?
- Does each claim match its evidence, with one hedge at most?
- Is each result exact, with the number, the condition and the comparison?
- Is each term defined once and then used in the same way?
- Is the work of the authors in the active voice, with "we"?
- Is there a figure of speech, a hype word or a long word with a short equivalent? Replace it.
- Does each sentence follow from the one before it?
- Are the limitations specific and stated openly?

## Examples

**Abstract sentence**

Before:
> In this paper, we propose a novel and comprehensive framework that leverages state-of-the-art transformer architectures in order to facilitate significantly improved performance on the task of clinical text summarization.

After:
> We fine-tune a 1.3-billion-parameter transformer to summarise radiology reports and compare it with three published baselines.

**Result**

Before:
> The results clearly demonstrate that our approach significantly outperforms existing methods across the board.

After:
> Our model reaches a ROUGE-L of 41.2 on the test set, compared with 37.9 for the strongest baseline (Table 2). The gain is largest for long reports, which suggests that the model handles long inputs better than the baselines do.

**Hedge matched to the evidence**

Before:
> This proves that larger models learn more general representations.

After:
> This result is consistent with the idea that larger models learn more general representations, but our experiments do not test this idea directly.

**Related work**

Before:
> A growing body of literature has shed light on the pivotal role that pre-training plays in the realm of NLP.

After:
> Pre-training on large text corpora improves results on many NLP tasks [CITE: BERT, GPT-2, T5].

**Limitation**

Before:
> It should be noted that the study may potentially have certain limitations with regard to generalizability.

After:
> All 84 pupils came from three schools in one city, so the results may not hold for other regions or age groups.
