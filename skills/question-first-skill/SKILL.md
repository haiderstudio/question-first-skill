---
name: question-first-skill
description: Ask before coding — turn a vague task into a one-page plan. Use when a coding task is vague, or when you are about to code from a brief you do not fully understand. Asks at most 5 questions, writes a one-page plan, then stops. Never codes from a vague brief, never invents requirements, never guesses.
---

# question-first-skill

Ask first, code later. When a task is vague, ask the few
questions that matter, write a one-page plan, and stop.
No code until the user approves the plan.

## When to use this skill

Use it when the user asks to:
- Build, add, change, or fix something, and the task as
  written leaves out what to build, where, or what counts
  as done.
- Start coding from a one-line brief, a chat message, or a
  rough idea.
- Plan a change before writing any code.

## When NOT to use it

- Do not use it for a task that is already clear: what to
  build, where it goes, and what counts as done are all
  stated. Go straight to step 3 and write the plan, with
  zero questions.
- Do not use it for a question with no code in it ("how
  does this work?", "why did this fail?"). Answer the
  question; there is nothing to plan.
- Do not use it to write a full design doc, a spec, or a
  multi-page plan. One page is the whole output.
- Do not use it as a code review, a bug hunt, or a refactor
  plan for code that already exists. Those are separate jobs.

## Workflow

### 1. Read the task as written

1. Copy the task in the user's own words. Do not rewrite it.
2. Judge it against three checks:
   - What is to be built or changed?
   - Where does it go (which files, or which part of the app)?
   - What counts as done (how will anyone tell it works)?
3. If all three have answers in the task, the task is clear.
   Skip step 2 and write the plan.
4. If any one is missing, the task is vague. Go to step 2.

### 2. Ask at most 5 questions, one round only

1. Ask only questions whose answer could change what gets
   built. If the answer would not change the plan, do not ask.
2. Ask at most 5 questions, in one round. Never a second
   round, never a follow-up round to "be sure".
3. Offer 2–3 short options for each question where options
   exist, so the user can pick instead of writing an essay.
   An open question with no options is fine when the answer
   is a fact only the user knows.
4. Never ask about something you can read in the repo
   yourself: file names, existing behaviour, how the code
   is laid out. Read it, do not ask it.
5. If the user will not answer, or says "just do it", stop.
   Say what is still missing. Do not guess, do not code.

### 3. Write a one-page plan, then stop

Write the plan in this fixed shape, and no other shape:

```markdown
Task: <the task, in the user's own words>
Goal: <one sentence>
Questions asked: <0 to 5, each with the answer given>
What changes: <files or areas, named>
What does not change: <named>
Steps: <numbered, at most 7>
Checks: <how to tell it works>
Open questions: <only ones left unanswered, marked unanswered>
```

Rules for the plan:

- One page means at most 50 lines. If it does not fit,
  cut detail. Never add a second page.
- Every line must trace to the task, the user's answers,
  or the code you read. A line that traces to none of
  those is invented — delete it.
- An unanswered question stays listed under "Open
  questions", marked unanswered. Never fill it in with
  a guess.
- Then stop. Do not write code, do not edit a file, do
  not run a command that changes anything. The plan is
  the output. Code starts only when the user says so,
  in plain words ("build it", "go ahead", "approved").

## Good examples

A vague brief, 4 questions, one-page plan (full worked
example in `examples/sample-plan.md`, from the brief in
`examples/vague-brief.md`):

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

A clear task gets zero questions and goes straight to a plan
(full worked example in `examples/clear-brief-plan.md`):

```markdown
Task: Add a clear command to the sample app that deletes all
done tasks and prints how many were deleted.
Goal: One command clears done tasks and reports the count.
Questions asked: None — the task states what, where, and done.
What changes: app.py (new clear command).
What does not change: tasks.json format, the other commands.
Steps:
1. Read tasks.json.
2. Remove tasks marked done.
3. Write tasks.json back.
4. Print "Deleted N done tasks."
Checks: After clear, list shows no done tasks; the printed
count matches the number removed.
Open questions: None.
```

## Bad examples (do not write like this)

> `Add login to the sample app.` → writes code with JWT
> tokens, email verification, and a password reset page.

The brief said none of those things. Every one of them is
invented. Ask first, or stop.

> Asks 12 questions about login, then asks 4 more "to be
> sure", then writes a 3-page spec.

More than 5 questions, a second round, and more than one
page. The cap is the job.

> Writes the plan, then writes the code anyway, without
> the user saying so.

The plan is the output. Code without approval is the exact
thing this skill stops.

## Output rules

- Output one plan per task, in its own code block.
- Every line in the plan must trace to the task, an answer,
  or the code you read. If it cannot be traced, leave it out.
- Never invent a requirement, a file, a behaviour, or a
  value the user did not give and the code does not show.
- Never claim a check was run, a file was read, or a user
  agreed to something, unless it actually happened.
- Never write code, edit a file, or run a command that
  changes anything, until the user approves the plan in
  plain words.

## Limits and safety rules

- This skill reads the task and the repo only. It sends
  nothing anywhere, edits no file, and needs no API key
  or secret.
- It asks at most 5 questions, in one round only. It writes
  at most one page. Those caps are hard limits, not targets.
- It never guesses. A missing answer is listed as an open
  question, never filled in.
- It never codes from a vague brief. If the brief is vague
  and the user will not answer, the skill stops and says
  what is missing.
- The plan is not a promise that the build will work. It is
  a record of what was asked, what was answered, and what
  is still open.
