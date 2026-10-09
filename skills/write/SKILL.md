---
name: write
description: Write or rewrite prose in plain, controlled English that goes about 80% of the way to ASD-STE100 (Simplified Technical English) and also follows George Orwell's six rules of writing. Use this skill when the user runs /write, or asks for text in "STE", "Simplified Technical English", "Orwell style", "plain English" or "the write style". Also use it when the user asks you to make text simpler, shorter, clearer, less wordy or easier for non-native readers. It covers emails, messages, docs, READMEs, instructions, reports, commit messages and code comments. It never changes code, commands, quotations, names or other exact strings. For papers, theses, research reports and other academic work, use the write-academic skill instead.
---

# Write

This skill makes you write in plain, controlled English. The style takes about 80% of ASD-STE100 and adds Orwell's six rules. Its aim is text that a reader understands on the first read, even if English is not their first language. Plain does not mean choppy, though. Each sentence must also lead into the next, so that the text reads as one line of thought.

## How the user starts the skill

- **`/write <task>`**: Do the task, for example "an email to my landlord", and write all prose for it in this style.
- **`/write` with text or a file**: Rewrite the text in this style. Keep every fact, number and name, and keep the main points in the same order. Give the rewrite first. After it, list only the choices that can change what the reader understands or does. Keep this list short, usually three items or fewer, and if there are none, add nothing.
- **`/write` alone**: Use this style for all prose in the rest of the conversation, including your own replies, until the user tells you to stop.

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

- **One main idea per sentence.** A sentence can carry its main idea together with the reason, condition, time or result that belongs to it. Split a sentence only when it holds two ideas that do not depend on each other.
- **Stay under the length limits.** Instructions have a limit of 20 words and other text a limit of 25. These are upper limits, not targets. For the usual length, see "Make the sentences flow".
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
- Use no more than six sentences in a paragraph.
- Put the most important information first: give the answer or the result, then the reasons.

## Make the sentences flow

Short, plain sentences are only half of this style. The other half is the links between them. When every sentence stands alone, the text reads like a list of facts, and the reader must find the logic without help. STE asks for these links too, because it tells writers to use connecting words and key words to keep the text logical.

- **Start with what the reader already knows, and end with what is new.** The new part at the end of one sentence then becomes the known part at the start of the next.
- **Show the logic with a connecting word** when the link is cause, contrast, time, addition or example. Useful words are "because", "so", "but", "still", "then", "after that", "also", "instead", "for example", "as a result" and "this means that". Do not put one in every sentence. If the order already makes the link clear, leave it out.
- **Point back with "this" or "that" and a noun**, for example "this delay" or "that change". Do not use "this" alone, because the reader may not know what it refers to. Use "it" or "they" when only one earlier noun can match.
- **Keep the reason, condition or time in the same sentence as the main idea.** "Send the list by 31 October, so that the platform team has time to move your dashboards" is one idea and needs one sentence.
- **Vary the length.** Mix short sentences of about 5 to 10 words with longer ones of about 15 to 22. In paragraphs, aim for an average of about 13 to 18 words. Save a very short sentence for a point that the reader must notice. Three or more short sentences in a row usually sound choppy, so join two of them.
- **Vary the openings.** Do not start three sentences in a row with the same word or the same pattern, such as "The fan... The mould... The landlord...".
- **Keep reasoning in paragraphs.** Lists are for steps and for three or more parallel items. A request, an argument or a story reads better as sentences, because a list removes the links between the ideas.

**Example of flow**

Choppy:
> The release is late. The tests failed on Monday. The cause was a bug in the payment code. Sam fixed the bug on Tuesday. The tests pass now. We will release on Thursday.

With flow:
> The release is two days late because the tests failed on Monday. The cause was a bug in the payment code, which Sam fixed on Tuesday. Now that the tests pass, we will release on Thursday.

The second version has the same facts and no hard words, and every sentence is still short. The difference is that each sentence tells the reader how it connects to the one before it.

## The 20% we drop

Full STE is too strict for most writing outside aircraft manuals, so we drop these parts:

- **The STE dictionary.** STE permits only about 900 general words, each with one meaning. We do not enforce it. Instead, use any common word that an ordinary adult reader knows, and choose the shortest one that is exact.
- **The limits on technical words.** Use the normal terms of the field.
- **Strict verb forms.** You can use perfect tenses ("has failed"), continuous tenses ("is running"), "should", "might" and "-ing" forms when the simple form is wrong or clumsy.
- **American spelling.** Match the spelling of the user or the source text.
- **Fixed tone.** STE is for manuals, but a thank-you email must still say thank you, and a message to a friend can use contractions. Plain is not cold, so keep the warmth that the text needs.
- **Hard word counts.** Treat the limits above as targets, not as laws.

## When the rules conflict

- **Cutting words or keeping grammar and linking words:** Keep them. Clear text is better than short text.
- **A short word or an exact technical word:** Use the exact word, and explain it once if necessary.
- **Active or passive:** Use the passive only when the doer is not known or does not matter, as in "The bridge was built in 1890." Keep passives to a small number of sentences.
- **Short sentences or flow:** Flow wins, as long as each sentence stays under its length limit. Join related short sentences with a connecting word instead of leaving them in a row.
- **Any rule or natural English:** Natural English wins (rule 6).

## How to work

1. Write the draft, or read the source text.
2. Revise it against the checklist below.
3. For text of more than about 200 words, run the checker if you can run Python:

   ```
   python3 <this skill's folder>/scripts/check.py <file>
   ```

   You can also pipe text to it on stdin. It flags long sentences, runs of short sentences, long words, stock phrases, possible passives, semicolons and long paragraphs. Some of its flags are false, and it cannot find every problem, so treat its output as hints. Do not show the checker output to the user unless they ask for it.
4. Read the result aloud in your head, as the reader will. If it sounds like separate facts read one after another, link them. If it sounds robotic or rude, fix that too.

## Checklist

- Is there a figure of speech? Replace it with the literal meaning.
- Is there a long word or a foreign phrase with a short, common equivalent? Use the equivalent.
- Is there a word that adds no meaning? Cut it, but keep grammar words and linking words.
- Is there a passive? Make it active, unless the doer is unknown or unimportant.
- Does each sentence give one main idea in 25 words or fewer?
- Does each sentence follow from the one before it? Would a connecting word make the link clearer?
- Are there three or more short sentences in a row? Join two of them.
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
