#!/usr/bin/env python3
"""Check text against the main rules of the "write" styles.

Usage:
    python3 check.py [--profile plain|academic] [FILE ...]
    cat draft.md | python3 check.py --profile academic

The script flags long sentences, runs of short sentences, long paragraphs,
semicolons, possible passives and the words and phrases in the word list
of the skill that holds this script (references/word-list.md). The
"academic" profile allows longer sentences and paragraphs and reads LaTeX.
The script skips code, maths, citations, URLs and headings.

It gives hints only. Some flags are false, and it cannot find figures of
speech that are not in the list, noun clusters or changes of term.
"""

import argparse
import re
import sys
from pathlib import Path

PROFILES = {
    "plain": {
        "sentence_limit": 25,     # words, descriptive text
        "step_limit": 20,         # words, items in a numbered list
        "paragraph_limit": 6,     # sentences
        "short_sentence": 10,     # words or fewer counts as a short sentence
        "choppy_run": 3,          # this many short sentences in a row sounds choppy
        "average_min": 11,        # words, average for sentences in paragraphs
        "average_max": None,
        "aim": "13 to 18",
        "semicolons_per_paragraph": 0,
    },
    "academic": {
        "sentence_limit": 35,
        "step_limit": 25,
        "paragraph_limit": 8,
        "short_sentence": 10,
        "choppy_run": 3,
        "average_min": 15,
        "average_max": 27,
        "aim": "18 to 26",
        "semicolons_per_paragraph": 1,
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
             "prose_sentences": 0, "prose_words": 0}
    for line, block, kind in blocks(text.splitlines()):
        sentences = split_sentences(block)
        if kind != "step" and len(sentences) > profile["paragraph_limit"]:
            findings.append((line, "long paragraph",
                             f"{len(sentences)} sentences, limit {profile['paragraph_limit']}"))
        if kind != "step":
            for run in choppy_runs(sentences, profile):
                findings.append((line, "choppy",
                                 f"{len(run)} short sentences in a row: {preview(' '.join(run))}"))
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
            limit = profile["step_limit"] if kind == "step" else profile["sentence_limit"]
            if words > limit:
                findings.append((line, "long sentence",
                                 f"{words} words, limit {limit}: {preview(sentence)}"))
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
    if stats["prose_sentences"] >= 5:
        average = stats["prose_words"] / stats["prose_sentences"]
        if average < profile["average_min"]:
            findings.append((None, "short sentences overall",
                             f"paragraph sentences average {average:.1f} words, "
                             f"aim for {profile['aim']} and link them"))
        elif profile["average_max"] and average > profile["average_max"]:
            findings.append((None, "dense overall",
                             f"paragraph sentences average {average:.1f} words, "
                             f"aim for {profile['aim']} and split the longest ones"))
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
        print(f"-- {stats['sentences']} sentences, average {average:.1f} words "
              f"({prose:.1f} in paragraphs), "
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
