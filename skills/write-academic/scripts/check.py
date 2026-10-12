#!/usr/bin/env python3
"""Check text against the main rules of the "write" styles.

Usage:
    python3 check.py [--profile plain|academic] [FILE ...]
    cat draft.md | python3 check.py --profile academic

The script flags flat rhythm (sentences that are all about the same
length), runs of short sentences, sentences that start with the same
word, fragmented paragraphs, semicolons,
possible passives and the words and phrases in the word list
of the skill that holds this script (references/word-list.md). It never
enforces a word limit. The "academic" profile expects a wider range of
sentence lengths and allows the odd semicolon.
The script skips code, maths, citations, URLs and headings.

It gives hints only. Some flags are false, and it cannot find figures of
speech that are not in the list, noun clusters or changes of term.
"""

import argparse
import re
import statistics
import sys
from pathlib import Path

PROFILES = {
    # These numbers only detect choppy or flat rhythm. None of them is a limit
    # on how long a sentence or paragraph may be.
    "plain": {
        "short_sentence": 10,     # words or fewer counts as a short sentence
        "choppy_run": 3,          # this many short sentences in a row sounds choppy
        "long_sentence": 25,      # words or more counts as a long sentence
        "long_share_min": 0.10,   # rhythm is flat if fewer sentences than this are long
        "spread_min": 7.0,        # rhythm is flat if sentence lengths vary less than this
        "semicolons_per_paragraph": 0,
        "paragraph_mean_min": 2.5,  # sentences, average for paragraphs
        "repeat_run": 3,          # this many sentences in a row with the same first word
    },
    "academic": {
        "short_sentence": 10,
        "choppy_run": 3,
        "long_sentence": 28,
        "long_share_min": 0.10,
        "spread_min": 7.5,
        "semicolons_per_paragraph": 1,
        "paragraph_mean_min": 3.0,
        "repeat_run": 3,
    },
}

WORD_LIST = Path(__file__).resolve().parent.parent / "references" / "word-list.md"

SECTION_LABELS = {
    "long words": "long word",
    "wordy phrases": "wordy phrase",
    "stock figures of speech": "stock figure of speech",
    "jargon and foreign phrases": "jargon",
    "weak connecting words": "weak connecting word",
    "hype and filler": "hype",
}

ABBREVIATIONS = ["e.g.", "i.e.", "etc.", "vs.", "viz.", "Mr.", "Mrs.", "Ms.",
                 "Dr.", "St.", "No.", "approx.", "cf.", "Fig.", "Figs.", "Inc.",
                 "Ltd.", "et al.", "Eq.", "Eqs.", "Sec.", "Tab.", "Ref.",
                 "Refs.", "resp.", "Proc.", "Vol.", "pp."]

IRREGULAR_PARTICIPLES = {
    "been", "begun", "bitten", "blown", "born", "borne", "bought", "broken",
    "brought", "built", "caught", "chosen", "come", "cut", "done", "drawn",
    "driven", "eaten", "fallen", "felt", "forbidden", "forgotten", "found",
    "frozen", "given", "gone", "grown", "heard", "held", "hidden", "hit",
    "hung", "hurt", "kept", "known", "laid", "led", "left", "lent", "let",
    "lost", "made", "meant", "met", "paid", "put", "read", "run", "said",
    "seen", "sent", "set", "shown", "shut", "sold", "spent", "split",
    "spoken", "spread", "stolen", "struck", "sung", "taken", "taught",
    "thought", "thrown", "told", "understood", "won", "worn", "written",
}
NOT_PARTICIPLES = {"need", "red", "bed", "feed", "seed", "speed", "indeed",
                   "hundred", "shed", "weed", "proceed", "exceed", "succeed"}

PASSIVE = re.compile(
    r"\b(am|is|are|was|were|be|been|being|get|gets|got|gotten)\s+"
    r"(?:\w+ly\s+)?(\w+)\b",
    re.IGNORECASE,
)
WORD = re.compile(r"[A-Za-z0-9][\w'’.\-]*")
LIST_ITEM = re.compile(r"^\s*(?:([-*+])|(\d+)[.)])\s+")
SENTENCE_END = re.compile(r"(?<=[.!?])[\"')\]]*\s+(?=[\"'(\[]?[A-Z0-9])")

LATEX_HEADING = re.compile(r"^\\(part|chapter|section|subsection|subsubsection|paragraph|title|caption)\*?[\[{]")
LATEX_SKIP_ENV = re.compile(
    r"\\begin\{(equation|align|gather|multline|eqnarray|figure|table|tabular|"
    r"algorithm|algorithmic|lstlisting|verbatim|minted|thebibliography)\*?\}")


def load_word_list(path):
    """Return a list of (compiled pattern, phrase, swap, label)."""
    entries = []
    label = "word list"
    if not path.exists():
        return entries
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            label = SECTION_LABELS.get(line[3:].strip().lower(), "word list")
            continue
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() == "avoid":
            continue
        phrase, swap = cells[0], cells[1]
        entries.append((phrase_pattern(phrase), phrase, swap, label))
    return entries


def phrase_pattern(phrase):
    """Match a phrase, and the usual inflections of a single word."""
    if re.fullmatch(r"[a-z]+", phrase):
        if phrase.endswith("e"):
            body = re.escape(phrase[:-1]) + "(?:e|es|ed|ing)"
        else:
            body = re.escape(phrase) + "(?:s|es|ed|ing)?"
        body = body.replace("iz", "i[sz]")
    else:
        body = re.escape(phrase).replace(r"\ ", r"\s+")
    return re.compile(r"(?<!\w)" + body + r"(?!\w)", re.IGNORECASE)


def clean(text):
    """Remove the parts of a line that are not prose."""
    text = re.sub(r"`[^`]*`", "CODE", text)
    text = re.sub(r"\$[^$]*\$", "MATH", text)
    text = re.sub(r"\\cite[a-z]*\*?(\[[^\]]*\])*\{[^}]*\}", "", text)
    text = re.sub(r"\\(eq|auto|c|C)?ref\{[^}]*\}", "1", text)
    text = re.sub(r"\\label\{[^}]*\}", "", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?\{([^{}]*)\}", r"\2", text)
    text = re.sub(r"\\[a-zA-Z]+\*?", "", text)
    text = re.sub(r"\[@[^\]]*\]", "", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", "URL", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_]{1,3}", "", text)
    return text.replace("~", " ")


def blocks(lines):
    """Yield (first line number, text, kind) for each prose block.

    A block is a paragraph or one list item. The kind is "paragraph",
    "bullet" or "step" (an item in a numbered list). Code, maths, headings,
    tables and rules are skipped.
    """
    in_code = False
    skip_env = None
    current, start, kind = [], 0, "paragraph"

    def flush():
        if current:
            yield start, " ".join(current), kind

    for number, raw in enumerate(lines, 1):
        stripped = raw.strip()
        if stripped.startswith(("```", "~~~")):
            yield from flush()
            current = []
            in_code = not in_code
            continue
        if in_code:
            continue
        if skip_env:
            if f"\\end{{{skip_env}" in stripped:
                skip_env = None
            continue
        env = LATEX_SKIP_ENV.search(stripped)
        if env or stripped.startswith(("\\[", "$$")):
            yield from flush()
            current = []
            if env and f"\\end{{{env.group(1)}" not in stripped:
                skip_env = env.group(1)
            continue
        line = re.sub(r"^\s*>\s?", "", raw).rstrip()
        line = re.sub(r"^\s*\\item\s*", "- ", line)
        stripped = line.strip()
        if (not stripped or stripped.startswith(("#", "|", "---", "***", "%", "\\begin", "\\end"))
                or LATEX_HEADING.match(stripped)):
            yield from flush()
            current = []
            continue
        item = LIST_ITEM.match(line)
        if item:
            yield from flush()
            current, start = [clean(line[item.end():])], number
            kind = "step" if item.group(2) else "bullet"
            continue
        if not current:
            start, kind = number, "paragraph"
        current.append(clean(stripped))
    yield from flush()


def split_sentences(text):
    protected = text
    for abbr in ABBREVIATIONS:
        protected = re.sub(r"(?<!\w)" + re.escape(abbr),
                           abbr.replace(".", "\u2024"), protected)
    parts = SENTENCE_END.split(protected)
    return [p.replace("\u2024", ".").strip() for p in parts if p.strip()]


def choppy_runs(sentences, profile):
    """Yield each run of short sentences that is long enough to sound choppy."""
    run = []
    for sentence in sentences + [""]:
        if sentence and len(WORD.findall(sentence)) <= profile["short_sentence"]:
            run.append(sentence)
            continue
        if len(run) >= profile["choppy_run"]:
            yield run
        run = []


def repeated_openings(sentences, profile):
    """Yield each run of sentences in a row that start with the same word."""
    run, last = [], None
    for sentence in sentences + [""]:
        words = WORD.findall(sentence)
        first = words[0].lower() if words else None
        if first and first == last:
            run.append(sentence)
            continue
        if len(run) >= profile["repeat_run"]:
            yield run
        run, last = ([sentence], first) if first else ([], None)


def ends_like_prose(block):
    """True for a paragraph that ends a sentence, not for a greeting or sign-off."""
    return bool(re.search(r"[.!?][\"')\]]*\s*$", block.strip()))


def strip_front_matter(text):
    """Blank out YAML front matter, but keep the line numbers."""
    match = re.match(r"---\n.*?\n---\n", text, re.DOTALL)
    if not match:
        return text
    return "\n" * match.group(0).count("\n") + text[match.end():]


def check(text, word_list, profile=PROFILES["plain"]):
    text = strip_front_matter(text)
    findings = []
    stats = {"sentences": 0, "words": 0, "longest": 0, "passives": 0,
             "prose_sentences": 0, "prose_words": 0, "paragraphs": [], "lengths": []}
    for line, block, kind in blocks(text.splitlines()):
        sentences = split_sentences(block)
        if kind != "step":
            for run in choppy_runs(sentences, profile):
                findings.append((line, "choppy",
                                 f"{len(run)} short sentences in a row: {preview(' '.join(run))}"))
            for run in repeated_openings(sentences, profile):
                findings.append((line, "repeated openings",
                                 f"{len(run)} sentences in a row start with "
                                 f"\"{WORD.findall(run[0])[0]}\": {preview(' '.join(run))}"))
        if kind == "paragraph" and ends_like_prose(block) and len(WORD.findall(block)) >= 5:
            stats["paragraphs"].append(len(sentences))
        if block.count(";") > profile["semicolons_per_paragraph"]:
            findings.append((line, "semicolon",
                             f"{block.count(';')} in this paragraph, limit "
                             f"{profile['semicolons_per_paragraph']}: {preview(block)}"))
        for sentence in sentences:
            words = len(WORD.findall(sentence))
            if words == 0:
                continue
            stats["sentences"] += 1
            stats["words"] += words
            stats["longest"] = max(stats["longest"], words)
            if kind == "paragraph":
                stats["prose_sentences"] += 1
                stats["prose_words"] += words
                stats["lengths"].append(words)
            for match in PASSIVE.finditer(sentence):
                word = match.group(2).lower()
                if word in NOT_PARTICIPLES:
                    continue
                if word.endswith("ed") or word in IRREGULAR_PARTICIPLES:
                    stats["passives"] += 1
                    findings.append((line, "possible passive", match.group(0)))
            for pattern, phrase, swap, label in word_list:
                for match in pattern.finditer(sentence):
                    findings.append((line, label, f'"{match.group(0)}" -> {swap}'))
    lengths = stats["lengths"]
    if len(lengths) >= 10:
        spread = statistics.pstdev(lengths)
        long_share = sum(n >= profile["long_sentence"] for n in lengths) / len(lengths)
        if spread < profile["spread_min"] or long_share < profile["long_share_min"]:
            findings.append((None, "flat rhythm",
                             "most sentences are about the same length; let the thought set the length, "
                             "so join linked ideas into longer sentences and keep a short one for a key point"))
    counts = stats["paragraphs"]
    if len(counts) >= 3 and counts[-1] == 1:
        counts = counts[:-1]  # a one-line closing, such as a thank-you, is fine
    if len(counts) >= 3:
        single = sum(n == 1 for n in counts)
        mean = sum(counts) / len(counts)
        if single * 3 > len(counts) or mean < profile["paragraph_mean_min"]:
            findings.append((None, "fragmented paragraphs",
                             f"{single} of {len(counts)} paragraphs have one sentence, "
                             f"average {mean:.1f} sentences per paragraph; "
                             f"join related sentences into paragraphs"))
    return findings, stats


def preview(sentence, width=70):
    return sentence if len(sentence) <= width else sentence[:width - 3] + "..."


def report(name, text, word_list, profile):
    findings, stats = check(text, word_list, profile)
    if name:
        print(f"== {name}")
    for line, kind, detail in findings:
        print(f"{'overall' if line is None else f'line {line}'}: {kind}: {detail}")
    if stats["sentences"]:
        average = stats["words"] / stats["sentences"]
        prose = stats["prose_words"] / max(stats["prose_sentences"], 1)
        counts = stats["paragraphs"]
        per_paragraph = sum(counts) / len(counts) if counts else 0
        lengths = stats["lengths"]
        spread = statistics.pstdev(lengths) if len(lengths) > 1 else 0
        print(f"-- {stats['sentences']} sentences, average {average:.1f} words "
              f"({prose:.1f} in paragraphs, spread {spread:.1f}), {per_paragraph:.1f} sentences per paragraph, "
              f"longest {stats['longest']}, possible passives {stats['passives']}, "
              f"{len(findings)} flags")
    else:
        print("-- no prose found")


def main(argv):
    parser = argparse.ArgumentParser(
        description=__doc__.strip().splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="\n".join(__doc__.strip().splitlines()[1:]))
    parser.add_argument("--profile", choices=sorted(PROFILES), default="plain")
    parser.add_argument("files", nargs="*", help="files to check (default: stdin)")
    args = parser.parse_args(argv[1:])
    profile = PROFILES[args.profile]
    word_list = load_word_list(WORD_LIST)
    if not args.files:
        report(None, sys.stdin.read(), word_list, profile)
    for name in args.files:
        report(name if len(args.files) > 1 else None,
               Path(name).read_text(encoding="utf-8"), word_list, profile)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
