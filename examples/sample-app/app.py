"""A tiny to-do list app. The sample app the skill walks through.

Commands:
  python3 app.py add "Buy milk"
  python3 app.py list
  python3 app.py done 1
Tasks are kept in tasks.json next to this file.
"""
import json
import sys
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    return json.loads(TASKS_FILE.read_text())


def save_tasks(tasks):
    TASKS_FILE.write_text(json.dumps(tasks, indent=2) + "\n")


def main(argv):
    tasks = load_tasks()
    if not argv or argv[0] == "list":
        for i, task in enumerate(tasks, 1):
            mark = "x" if task["done"] else " "
            print(f"{i}. [{mark}] {task['text']}")
        return 0
    if argv[0] == "add" and len(argv) > 1:
        tasks.append({"text": " ".join(argv[1:]), "done": False})
        save_tasks(tasks)
        print(f"Added task {len(tasks)}.")
        return 0
    if argv[0] == "done" and len(argv) > 1:
        index = int(argv[1]) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Task {argv[1]} done.")
        return 0
    print("Usage: app.py [list | add <text> | done <number>]")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
