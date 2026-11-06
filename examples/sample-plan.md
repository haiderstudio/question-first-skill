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
