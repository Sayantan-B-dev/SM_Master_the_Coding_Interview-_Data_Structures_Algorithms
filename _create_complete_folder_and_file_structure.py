#!/usr/bin/env python3
"""
create_course_tree.py

Reads #._output.txt (containing course structure) and creates a folder tree:
- Each section becomes a folder named "Section_XXX - SectionName"
- Inside each section folder, numbered lectures become files "XXX - Title.md"
- Coding Exercises, Quizzes, and Assignments become sequentially numbered files
  "XXX - Type Num Title.md", with auto‑incremented numbers.
Invalid filename characters are removed.
"""

import re
from pathlib import Path

def pad(num: int) -> str:
    """Return a zero‑padded three‑digit string of num."""
    return f"{num:03d}"

def sanitize(s: str) -> str:
    """Remove characters that are illegal in file names and normalise spaces."""
    s = re.sub(r'[\\/:*?"<>|]', '', s)      # remove forbidden chars
    s = re.sub(r'\s+', ' ', s)              # collapse multiple spaces
    return s.strip()

def main():
    input_file = "#._output.txt"
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found.")
        return

    current_section = None   # current folder path (relative)
    auto_counter = 0         # last used number for unnumbered items

    with open(input_file, 'r', encoding='utf-8') as f:
        for raw_line in f:
            line = raw_line.rstrip('\n')
            # ---- Section line ----
            m = re.match(r'^Section\s+([0-9]+):\s+(.*)$', line)
            if m:
                sec_num = int(m.group(1))
                sec_name = sanitize(m.group(2))
                sec_dir = f"Section_{pad(sec_num)} - {sec_name}"
                Path(sec_dir).mkdir(exist_ok=True)
                current_section = sec_dir
                auto_counter = 0
                continue

            # Skip lines before the first section
            if current_section is None:
                continue

            # ---- Numbered lecture ----
            m = re.match(r'^\s*([0-9]+)\.\s+(.*)$', line)
            if m:
                num = int(m.group(1))
                title = sanitize(m.group(2))
                filename = f"{pad(num)} - {title}.md"
                Path(current_section, filename).touch()
                auto_counter = num
                continue

            # ---- Coding Exercise / Quiz / Assignment ----
            m = re.match(r'^\s*(Coding Exercise|Quiz|Assignment)\s*([0-9]*):?\s*(.*)$', line)
            if m:
                type_ = m.group(1)
                num_str = m.group(2)
                title_extra = m.group(3)
                # Build the title by concatenating type, optional number, and extra text
                parts = [type_]
                if num_str:
                    parts.append(num_str)
                if title_extra:
                    parts.append(title_extra)
                title = sanitize(' '.join(parts))
                auto_counter += 1
                filename = f"{pad(auto_counter)} - {title}.md"
                Path(current_section, filename).touch()
                continue

    print("Course folder tree created successfully")

if __name__ == "__main__":
    main()