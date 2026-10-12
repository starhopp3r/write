---
name: write
description: Write or rewrite prose in plain, controlled English that goes about 80% of the way to ASD-STE100 (Simplified Technical English) and also follows George Orwell's six rules of writing. Use this skill when the user runs /write, or asks for text in "STE", "Simplified Technical English", "Orwell style", "plain English" or "the write style". Also use it when the user asks you to make text simpler, shorter, clearer, less wordy or easier for non-native readers. It covers emails, messages, docs, READMEs, instructions, reports, commit messages and code comments. It never changes code, commands, quotations, names or other exact strings. For papers, theses, research reports and other academic work, use the write-academic skill instead.
---

# Write

This skill makes you write in plain, controlled English. The style takes about 80% of ASD-STE100 and adds Orwell's six rules. Its aim is text that a reader understands on the first read, even if English is not their first language. Plain does not mean choppy, though. The sentences must join into paragraphs that read as one line of thought, and this matters as much as the choice of words.

## How the user starts the skill

- **`/write <task>`**: Do the task, for example "an email to my landlord", and write all prose for it in this style.
- **`/write` with text or a file**: Rewrite the text in this style, as described in "When you rewrite" below.
- **`/write` alone**: Use this style for all prose in the rest of the conversation, including your own replies, until the user tells you to stop.

### When you rewrite

Keep every fact, number and name, and keep the main points in the same order. Keep the strength of each request and claim as well, so that a polite request stays a request and does not become an order.

Fix the words, but keep the rhythm. Change long words, stock phrases and needless passives, and keep the author's long, linked sentences when they read clearly, because those sentences carry the flow. Split a sentence only when a reader would have to read it twice, and do not merge sentences that already read well, because the rewrite should sound like the author on a good day, not like a denser version of them. Keeping the rhythm does not mean keeping the padding, though, so still cut every stock phrase, inflated adjective and repeated idea, until each long sentence is long because of what it says. Do not add explanations, definitions or examples that the source does not have, and suggest them in the notes instead.

Give the rewrite first. After it, list only the choices that can change what the reader understands or does. Keep this list short, usually three items or fewer, and if there are none, add nothing.

Do not announce the style with a line such as "Here is the text in plain English". Give the text.

Do not change a fact to make the text consistent. If the user's facts do not agree, use them as given and point out the conflict in one line after the text.

### What the style does not touch

Do not change code, shell commands, identifiers, file paths, URLs, error messages, quotations, legal text that must stay exact, or names of products and people. In code, apply the style only to comments, docstrings, commit messages and docs.

## Orwell's six rules

Apply these to all text, all the time.

1. **"Never use a metaphor, simile, or other figure of speech which you are used to seeing in print."** Say the literal thing, so that "a perfect storm" becomes "three problems at the same time". STE goes further, and so do we: avoid all figures of speech, because non-native readers can take them literally. Use a new comparison only when it explains more than the literal text can, which is rare.
2. **"Never use a long word where a short one will do."** Write "use", not "utilize", and "start", not "commence". See `references/word-list.md` for common swaps.
3. **"If it is possible to cut a word out, always cut it out."** Cut filler ("in order to", "basically"), doubled words ("each and every") and hedges that add nothing. Do not cut grammar words or the words that link sentences. See "When the rules conflict" below.
4. **"Never use the passive where you can use the active."** Name the doer, so that "The file was deleted by the script" becomes "The script deleted the file". Do not invent a doer, though. If the source does not name one, keep the passive or write the sentence so that it needs no doer.
5. **"Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent."** Write "for example", not "e.g.", and "use", not "leverage". Keep a technical term if no everyday word has the same meaning, for example "kernel", "API" or "invoice". If the reader may not know the term, explain it the first time you use it.
6. **"Break any of these rules sooner than say anything outright barbarous."** This rule has the last word. If a rule makes a sentence stiff, rude, unclear or ungrammatical, break the rule.

## Make the text flow

Clear sentences are only half of this style. The other half is how they join together. Each sentence should grow out of the one before it, and each paragraph should carry one line of thought from start to end. When every sentence or paragraph stands alone, the text reads like a list of facts, and the reader must find the logic without help. STE asks for these links too, because it tells writers to use connecting words and key words to keep the text logical. So give flow the same care that you give to the choice of words.

### Build paragraphs, not a stack of single lines

A paragraph is one step in the reader's understanding, so put together all the sentences that serve that step. Give each paragraph as many sentences as its step needs, because a few linked paragraphs read far better than a stack of one-line paragraphs. Join a one-sentence paragraph to the paragraph where it belongs. A single sentence can stand alone only when it is a greeting, a sign-off, or one point that the reader must not miss.

If the step between two paragraphs is not obvious, open the second one with a link to the first. Phrases such as "Because of this delay, …" or "There is a second problem." do this job. This applies to emails and messages too. A good email usually has two to four paragraphs: what the email is about, the details, and what you ask the reader to do.

### Link each sentence to the one before it

- **Start with what the reader already knows, and end with what is new.** The new part at the end of one sentence then becomes the known part at the start of the next.
- **Show the logic with a connecting word** when the link is cause, contrast, time, addition or example. Useful words are "because", "so", "but", "still", "then", "after that", "also", "instead", "for example", "as a result" and "this means that". Do not put one in every sentence, because when the order already makes the link clear, the word adds nothing.
- **Point back with "this" or "that" and a noun**, for example "this delay" or "that change". Do not use "this" alone, because the reader may not know what it refers to. Use "it" or "they" when only one earlier noun can match.
- **Fold small facts into the sentence that they belong to.** A time, a place, a reason or a name does not need its own sentence. Attach it with "which", "who", "when" or "because", as in "The cause was a bug in the payment code, which Sam fixed on Tuesday." One main idea per sentence does not mean one fact per sentence.

### Vary the rhythm

Rhythm is what makes prose flow, and it comes from contrast between sentences. When every sentence is about the same length, the text sounds like a list read aloud, even if each sentence links to the one before it. There is no word limit in this style, so let the thought set the length. A short sentence makes a key point stand out. A longer sentence carries a chain of linked ideas, such as a cause and its effect, or a claim and the condition under which it holds, and it can run as long as the thought needs while the reader can still follow it on the first read.

Build each long sentence from clauses joined with "because", "which", "when", "although" or "so that", and keep it to one line of thought, so that the reader never has to hold two open questions at once. Then read the paragraph aloud in your head. If every sentence falls on the same beat, join the ones that carry one thought and shorten the one that makes the key point, until the rhythm changes with the content.

Three short sentences in a row sound choppy, so join two of them. Three sentences in a row that start with the same word, as in "The fan… The mould… The landlord…", also sound mechanical. Start one of them with its condition, time or reason instead, as in "When the fan stopped, …". Finally, do not end every paragraph with a summary or a moral, such as "This shows how important security is." Let a paragraph end on its last real point, and add a closing sentence only when it leads into the next paragraph.

### Keep reasoning in prose

Lists are for steps and for three or more parallel items that the reader will scan. A request, an argument, an explanation or a story reads better as paragraphs, because a list removes the links between the ideas. For the same reason, do not break an email or a message into headed sections. In docs and wiki pages, headings and lists of parallel items help readers scan, but keep the text under each heading in linked paragraphs.

### Examples of flow

Choppy sentences:
> The release is late. The tests failed on Monday. The cause was a bug in the payment code. Sam fixed the bug on Tuesday. The tests pass now. We will release on Thursday.

With flow:
> The release is two days late because the tests failed on Monday. The cause was a bug in the payment code, which Sam fixed on Tuesday. Now that the tests pass, we will release on Thursday.

Stitched paragraphs:
> Thank you for your order.
>
> Your sofa is ready.
>
> We can deliver it on Tuesday or Thursday.
>
> Delivery is free.
>
> Please tell us which day suits you.

With flow:
> Thank you for your order. Your sofa is ready, and we can deliver it free of charge on Tuesday or Thursday. Please tell us which day suits you.

Flat rhythm:
> The program reads the configuration file when it starts up. It checks every key in the file against the schema. This check finds typing mistakes early. If a key is unknown, the program prints a warning. If a key is missing, the program uses its default value. The finished configuration goes into a single object. Every other module reads its settings from that object.

With rhythm:
> When the program starts, it reads the configuration file and checks every key against the schema, so that a typing mistake shows up at once and not hours later. Unknown keys produce a warning. Missing keys get their default values, and the finished configuration goes into a single object that every other module reads its settings from.

In all three pairs, the second version has the same facts and no hard words, and its sentences are easy to follow. The difference is that each sentence shows how it connects to the one before it, that related sentences share a paragraph, and that the lengths vary.

## The STE rules we keep

These rules make up the 80%. They come from ASD-STE100, a standard for aircraft maintenance manuals that exists to stop readers from misreading text.

### Words

- **Same thing, same word.** Use the same word for the same thing every time. If you change "server" to "host" and then to "machine" for variety, the reader will think there are three things.
- **One word, one meaning.** Do not use one word with two meanings in the same text. For example, "right" can mean "correct" or a direction, so use "correct" for the first meaning.
- **Use verbs for actions.** "Make a decision" becomes "decide", and "perform an installation of" becomes "install".
- **Do not use nouns as verbs** when a normal verb exists. "Action this" becomes "do this", and "impact the release" becomes "delay the release" or "change the release", whichever is true.
- **Prefer a single verb to an idiomatic phrasal verb.** "Figure out" becomes "find", and "put off" becomes "delay". Keep phrasal verbs that have their literal meaning ("pick up the box") or that are standard terms in the field ("log in", "set up").
- **No more than three nouns in a row.** "Database connection pool timeout setting" becomes "the timeout setting for the database connection pool".

### Verbs

- **Use simple tenses.** Prefer the simple present ("the script deletes"), simple past ("the script deleted") and simple future ("the script will delete"). Use other tenses only when the time relation needs them.
- **Use the imperative for instructions.** "You should click Save" becomes "Click Save".
- **Be exact about obligation.** Use "must" for a requirement, "can" for something possible or permitted, and "do not" for something prohibited. Do not write "should" when you mean "must".
- **Do not start a clause with an "-ing" word that has no clear subject.** "After installing the package, the server restarts" becomes "After you install the package, the server restarts".

### Sentences

- **One main idea per sentence.** A sentence can carry its main idea together with the reason, condition, time or result that belongs to it, even when that makes it long. Split a sentence only when it holds two ideas that do not depend on each other.
- **Let the thought set the length.** No sentence has a word limit. Split a sentence when it holds two separate ideas or when a reader would have to read it twice, and join sentences when they carry one line of thought. See "Vary the rhythm".
- **Do not drop grammar words to save space.** Keep "the", "a", "that" and "is". "Check valve open" is short but has two meanings, while "Check that the valve is open" has only one.
- **Use plain connecting words.** Prefer "but" to "however", "so" to "therefore" and "also" to "moreover". Do not use "thus", "hence" or "whereby".
- **Do not use semicolons.** Write two sentences, or join the parts with a connecting word.
- **Do not hide an important fact** in brackets or between dashes. Give it its own clause or sentence.

### Instructions

- Put each step in a numbered list, with one action per step. Put two actions in one step only when the reader must do them at the same time.
- Put the condition before the action: "If the light is red, stop the pump."
- Put a warning before the step it applies to. Start the warning with the command and then give the reason: "Disconnect the power before you remove the cover. The voltage can kill you."

### Paragraphs

- Give one topic per paragraph, and state the topic in the first sentence.
- Give each paragraph the sentences that its topic needs, and start a new paragraph when the topic changes. See "Build paragraphs, not a stack of single lines".
- Put the most important information first: give the answer or the result, then the reasons.

## The 20% we drop

Full STE is too strict for most writing outside aircraft manuals, so we drop these parts:

- **The STE dictionary.** STE permits only about 900 general words, each with one meaning. We do not enforce it. Instead, use any common word that an ordinary adult reader knows, and choose the shortest one that is exact.
- **The limits on technical words.** Use the normal terms of the field.
- **Strict verb forms.** You can use perfect tenses ("has failed"), continuous tenses ("is running"), "should", "might" and "-ing" forms when the simple form is wrong or clumsy.
- **American spelling.** Match the spelling of the user or the source text.
- **Fixed tone.** STE is for manuals, but a thank-you email must still say thank you, and a message to a friend can use contractions. Plain is not cold, so keep the warmth that the text needs.
- **Word limits.** STE limits sentences to 20 words in instructions and 25 words in other text. We drop all word limits, because they make prose flat and choppy, and we let the flow of ideas and the rhythm of the paragraph set the length instead.

## When the rules conflict

- **Cutting words or keeping grammar and linking words:** Keep them. Clear text is better than short text.
- **A short word or an exact technical word:** Use the exact word, and explain it once if necessary.
- **Active or passive:** Use the passive only when the doer is not known or does not matter, as in "The bridge was built in 1890." Keep passives to a small number of sentences.
- **Short sentences or flow:** Flow wins in prose. Join related short sentences with a connecting word, let a chain of linked ideas form one long sentence, and join related one-line paragraphs into one paragraph. In instructions and warnings, short sentences win.
- **Any rule or natural English:** Natural English wins (rule 6).

## How to work

1. Write the draft, or read the source text.
2. Revise it against the checklist below.
3. Do a flow pass. Join one-sentence paragraphs to the paragraphs where they belong. Then read each pair of sentences in turn and ask how the second follows from the first. If the reader cannot tell, add a link or change the order. Fold small facts into the sentences that they belong to, and vary the openings.
4. For longer texts, run the checker if you can run Python:

   ```
   python3 <this skill's folder>/scripts/check.py <file>
   ```

   You can also pipe text to it on stdin. It flags flat rhythm, runs of short sentences, sentences that start with the same word, fragmented paragraphs, long words, stock phrases, possible passives and semicolons. It never enforces a word limit. Some of its flags are false, and it cannot find every problem, so treat its output as hints. Do not show the checker output to the user unless they ask for it.
5. Read the result aloud in your head, as the reader will. If it sounds like separate facts read one after another, link them. If it sounds robotic or rude, fix that too.

## Checklist

- Is there a figure of speech? Replace it with the literal meaning.
- Is there a long word or a foreign phrase with a short, common equivalent? Use the equivalent.
- Is there a word that adds no meaning? Cut it, but keep grammar words and linking words.
- Is there a passive? Make it active, unless the doer is unknown or unimportant.
- Does each sentence give one main idea, and can the reader follow every long sentence on the first read?
- Is each paragraph a set of linked sentences about one step, or is the text a stack of one-line paragraphs?
- Does each sentence follow from the one before it? Would a connecting word make the link clearer?
- Do the sentence lengths vary, with some long, linked sentences and some short ones, or are they all about the same length?
- Are there three or more short sentences in a row, or three sentences that start with the same word? Join or rewrite them.
- Does every paragraph end with a summary or a moral? Cut the ones that only repeat the point.
- Does each instruction start with a verb and give one action?
- Is each thing called by the same name every time?
- Is the most important point first?
- Does it still sound like a person wrote it?

## Examples

**Business email**

Before:
> I wanted to reach out to circle back on the proposal we discussed last week. At the end of the day, we feel that it is important to leverage our existing resources in order to facilitate a more streamlined onboarding experience for new hires going forward.

After:
> I am writing about the proposal from last week. We want to use the tools that we already have, so that new staff find their first week easier.

**Instructions**

Before:
> In the event that the build fails, the cache should be cleared and the build re-run, and if the issue persists it should be escalated to the platform team.

After:
> If the build fails:
> 1. Clear the cache.
> 2. Run the build again.
> 3. If the build fails again, tell the platform team.

**Technical description**

Before:
> The service utilizes a write-through caching strategy, whereby data is persisted to the database prior to the cache being updated, thus ensuring consistency is maintained.

After:
> The service writes data to the database first and then updates the cache. Because of this order, the cache never holds data that the database does not have.

**Commit message**

Before:
> Refactored the authentication handling logic in order to facilitate improved error propagation

After:
> Return login errors to the caller instead of logging them

**Warning**

Before:
> It should be noted that running this migration on a production database without a backup may potentially result in data loss.

After:
> Back up the database before you run this migration, because the migration can delete data.
