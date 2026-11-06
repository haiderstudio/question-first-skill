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
