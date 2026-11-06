# question-first-skill

Ask before coding — turn a vague task into a one-page plan.

[![CI](https://github.com/haiderstudio/question-first-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/haiderstudio/question-first-skill/actions/workflows/ci.yml) [![Licence: MIT](https://img.shields.io/badge/Licence-MIT-yellow.svg)](LICENSE)

## What it does

When an AI coding agent loads this skill, it stops coding from
a vague brief. Instead it does one job, in this order:

1. Reads the task as written and judges it against three
   checks: what is to be built, where it goes, and what
   counts as done.
2. If any check has no answer, asks at most 5 questions, in
   one round only. Each question must be one whose answer
   could change what gets built.
3. Writes a one-page plan (at most 50 lines) in a fixed
   shape: goal, questions asked with answers, what changes,
   what does not change, steps, checks, and open questions.
4. Stops. No code until the user approves the plan in plain
   words.

A clear task gets zero questions and goes straight to the
plan. A vague task with no answers gets no code — the skill
stops and says what is still missing.

## What it does NOT do

- It does not write code, edit a file, or run a command that
  changes anything. The plan is the whole output.
- It does not ask more than 5 questions, ask a second round,
  or write more than one page. Those caps are hard limits.
- It does not invent requirements, files, behaviour, or
  values the user did not give and the code does not show.
- It does not write a full design doc, a spec, or a
  multi-page plan. One page is the whole output.
- It does not guess when the user will not answer. A missing
  answer stays listed as an open question, marked unanswered.

## Who it is for

Developers who use an AI coding agent and keep getting the
wrong thing built from a short brief — because the agent
guessed the missing parts instead of asking. This skill
makes the agent ask first, and makes the asking short: a
few questions, one page, then stop.

## How this differs from similar tools

Asking before coding is a known practice, and bigger tools
own the wide versions of it. This skill is the narrow one:

- Ponytail (DietrichGebert/ponytail, 185,470 stars, checked
  Nov 6, 2026) asks whether the code should exist at all and
  cuts code down. This skill does not judge the idea; it
  asks what the task means, then plans it in one page.
- Grill Me (mattpocock/grill-me, reported at over 130,000
  stars in June 2026 — I could not verify that number
  myself, the repo page did not load) interviews the user
  with 16 to 50 questions before any code. This skill asks
  at most 5, then stops asking.
- Zero-Assumption Development (marcel-silva/zero-assumption-
  development) is a full working method: inquiry, discovery,
  design, implementation, validation. This skill is one step
  of that kind of work — questions plus a one-page plan —
  and nothing after it.
- Superpowers' brainstorming skill writes a full design doc
  with 2–3 approaches and trade-offs. This skill writes one
  page, with one plan.

None of those were copied. The wording, the 5-question cap,
the 50-line page, and both worked examples here are original.

## Install

This skill follows the open Agent Skills format: a folder with a
`SKILL.md` file.

**Claude Code / Codex / Gemini CLI (project level):**

```bash
mkdir -p .agents/skills
cp -r skills/question-first-skill .agents/skills/question-first-skill
```

## Usage

Give the agent a task, in your own words, and tell it to use
this skill. The agent follows
`skills/question-first-skill/SKILL.md`: it judges the task,
asks at most 5 questions if the task is vague, writes a
one-page plan, and stops. No code is written until you say
"build it" or "approved".

## Example 1 — a vague brief

Task (from `examples/vague-brief.md`):

```text
Add login to the sample app.
```

The skill asks 4 questions, gets answers, and writes the
plan in `examples/sample-plan.md`:

```markdown
Task: Add login to the sample app.
Goal: Only a logged-in user can run the sample app's commands.
Questions asked:
1. How does a user log in? — Username and password.
2. Where are accounts kept? — A users.json file.
3. When is login checked? — Before any command runs.
4. What happens on a wrong password? — Print "wrong password" and stop.
What changes: app.py (check login first), users.json (new file).
What does not change: tasks.json, the add/list/done commands.
Steps:
1. Read users.json at start.
2. Ask for username and password.
3. Stop with "wrong password" if they do not match.
4. Run the command as before.
Checks: Wrong password stops the app; right password runs the command.
Open questions: None.
```

No JWT, no email check, no password reset page — the brief
and the answers said none of those things, so the plan has
none of them.

## Example 2 — a clear brief, zero questions

Task:

```text
Add a clear command to the sample app that deletes all done
tasks and prints how many were deleted.
```

The task states what, where, and what counts as done, so the
skill asks nothing and writes the plan straight away (full
plan in `examples/clear-brief-plan.md`):

```markdown
Task: Add a clear command to the sample app that deletes all done tasks and prints how many were deleted.
Goal: One command clears done tasks and reports the count.
Questions asked: None — the task states what, where, and done.
What changes: app.py (new clear command).
What does not change: tasks.json format, the other commands.
Steps:
1. Read tasks.json.
2. Remove tasks marked done.
3. Write tasks.json back.
4. Print "Deleted N done tasks."
Checks: After clear, list shows no done tasks; the printed count matches the number removed.
Open questions: None.
```

## How it is tested

```bash
python3 tests/test_skill.py
```

The tests check that `SKILL.md` has valid `name` and
`description` frontmatter and the required workflow sections;
that `.gitignore` starts with `.env`; that both example plans
have the fixed shape, fit in one page (at most 50 lines),
asked at most 5 questions, and contain no invented
requirements (no JWT, OAuth, email check, or password reset,
none of which the brief or the answers mention); and that
the sample app the walkthrough uses is real, runnable code.
No placeholder text anywhere in the repo.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and pull requests
are welcome; please keep examples real and checkable.

## Licence

MIT — see [LICENSE](LICENSE). This is original work. The
"ask before coding" practice is widely known; the related
tools named above are listed as related work, not sources —
nothing here was copied from them.
