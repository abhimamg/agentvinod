#!/usr/bin/env python3
"""
Workspace Summariser Script.

This script scans the workspace directories (strategy, ideas, events, tasks)
and prints a concise overview of available markdown files and action points.
"""

from pathlib import Path
import sys

DIRECTORIES = ["strategy", "ideas", "events", "tasks"]

def summarise_workspace() -> None:
    print("=== Personal Workspace Summary ===")
    root = Path(".")
    total_files = 0

    for idx, dir_name in enumerate(DIRECTORIES, 1):
        dir_path = root / dir_name
        files = [f for f in dir_path.glob("*.md")] if dir_path.exists() else []
        total_files += len(files)
        print(f"{idx}. {dir_name.capitalize()} ({len(files)} markdown file(s)):")
        if files:
            for f in files:
                print(f"   - {f.name}")
        else:
            print("   - No markdown files present.")

    print(f"\nTotal tracked markdown documents: {total_files}")

if __name__ == "__main__":
    summarise_workspace()
