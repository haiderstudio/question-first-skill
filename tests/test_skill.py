"""Tests for the question-first-skill: frontmatter, required sections,
.gitignore, the two worked plans (shape, one-page cap, question cap,
no invented requirements), README examples matching the real files,
and the sample app the walkthrough uses actually running."""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "question-first-skill" / "SKILL.md"
README = ROOT / "README.md"
PLAN = ROOT / "examples" / "sample-plan.md"
CLEAR_PLAN = ROOT / "examples" / "clear-brief-plan.md"
BRIEF = ROOT / "examples" / "vague-brief.md"
APP = ROOT / "examples" / "sample-app" / "app.py"
GITIGNORE = ROOT / ".gitignore"
CI = ROOT / ".github" / "workflows" / "ci.yml"
BANNED = ["TODO", "FIXME", "lorem", "coming soon"]
# Requirements the brief and the answers never mention. If a plan
# contains one, it was invented.
INVENTED = ["JWT", "OAuth", "email verification", "password reset"]
PLAN_SECTIONS = ["Task:", "Goal:", "Questions asked:", "What changes:",
                 "What does not change:", "Steps:", "Checks:",
                 "Open questions:"]


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        sys.exit(1)


def count_questions(plan_text):
    lines = plan_text.splitlines()
    start = next(i for i, line in enumerate(lines)
                 if line.startswith("Questions asked:"))
    count = 0
    for line in lines[start + 1:]:
        if re.match(r"^\d+\. ", line):
            count += 1
        elif line.startswith("What changes:"):
            break
    return count


def check_plan(name, path):
    text = path.read_text()
    lines = text.splitlines()
    check(name + "_sections", all(s in text for s in PLAN_SECTIONS))
    check(name + "_one_page", len(lines) <= 50)
    check(name + "_question_cap", count_questions(text) <= 5)
    check(name + "_no_invented",
          not any(term in text for term in INVENTED))
    check(name + "_in_readme", text.strip() in README.read_text())


def main():
    skill = SKILL.read_text()
    m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
    check("test_skill_frontmatter",
          bool(m) and "name: question-first-skill" in m.group(1)
          and "description:" in m.group(1))
    for section in ["When to use this skill", "When NOT to use it",
                    "Workflow", "Good examples", "Bad examples",
                    "Output rules", "Limits and safety rules"]:
        check("test_skill_sections_" + section.split()[0], section in skill)
    check("test_gitignore_env_first",
          GITIGNORE.read_text().splitlines()[0] == ".env")
    for f in [SKILL, README, PLAN, CLEAR_PLAN, BRIEF]:
        check("test_no_placeholders_" + f.name,
              not any(b in f.read_text() for b in BANNED))
    check("test_brief_is_vague",
          BRIEF.read_text().strip() == "Add login to the sample app.")
    check_plan("test_sample_plan", PLAN)
    check("test_sample_plan_asked_four", count_questions(PLAN.read_text()) == 4)
    check_plan("test_clear_plan", CLEAR_PLAN)
    check("test_clear_plan_asked_zero",
          count_questions(CLEAR_PLAN.read_text()) == 0)
    ci = yaml.safe_load(CI.read_text())
    check("test_ci_valid",
          ci["jobs"]["test"]["steps"][-1]["run"] == "python3 tests/test_skill.py")

    # The walkthrough sample app is real, runnable code.
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(APP, Path(tmp) / "app.py")

        def run(*args):
            out = subprocess.run([sys.executable, "app.py", *args],
                                 cwd=tmp, capture_output=True, text=True)
            check("test_app_runs_" + "_".join(args), out.returncode == 0)
            return out.stdout

        check("test_app_add", "Added task 1." in run("add", "Buy milk"))
        check("test_app_list", "[ ] Buy milk" in run("list"))
        check("test_app_done", "Task 1 done." in run("done", "1"))
        check("test_app_list_done", "[x] Buy milk" in run("list"))
    print("All tests passed.")


if __name__ == "__main__":
    main()
