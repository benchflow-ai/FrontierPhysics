#!/usr/bin/env python3
"""Enforce FrontierPhysics's current single-task public-repository contract."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_TASK = "surface-ion-trap-shuttling"


def main() -> int:
    problems: list[str] = []
    tasks_root = ROOT / "tasks"
    task_names = sorted(path.name for path in tasks_root.iterdir() if path.is_dir())

    if task_names != [EXPECTED_TASK]:
        problems.append(
            f"tasks/ must contain only {EXPECTED_TASK!r}; found {task_names}"
        )

    for forbidden in ("example_tasks", "tasks-extra"):
        if (ROOT / forbidden).exists():
            problems.append(f"forbidden public task directory exists: {forbidden}/")

    task_files = sorted(
        path
        for path in ROOT.glob("**/task.md")
        if ".venv" not in path.parts and ".git" not in path.parts
    )
    expected_file = tasks_root / EXPECTED_TASK / "task.md"
    if task_files != [expected_file]:
        problems.append(
            "exactly one task.md is allowed at "
            f"{expected_file.relative_to(ROOT)}; found "
            f"{[path.relative_to(ROOT).as_posix() for path in task_files]}"
        )

    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1

    print(f"OK: public repository contains exactly tasks/{EXPECTED_TASK}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
