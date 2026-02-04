#!/usr/bin/env python3
"""Generate a keyword ledger and concatenate all SKILL.md into an `mcp` file.

Writes:
- .github/skill_index/keyword_ledger.csv
- .github/skill_index/skills_index.csv
- mcp (workspace root) concatenation of all SKILL.md
"""
import os
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"
OUT_DIR = ROOT / ".github" / "skill_index"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def parse_frontmatter(lines):
    """Return dict of frontmatter keys (very small YAML-like parser)."""
    data = {}
    in_fm = False
    for line in lines:
        line = line.rstrip("\n")
        if line.strip() == "---":
            in_fm = not in_fm
            continue
        if not in_fm:
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            data[key] = val
    return data


def normalize_keywords(val):
    # expecting a YAML list like [a, b, c]
    v = val.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip() for p in inner.split(",")]
        # strip quotes
        parts = [p.strip("'\"") for p in parts]
        return parts
    return [v]


def main():
    skills = []
    for dirpath, dirnames, filenames in os.walk(SKILLS_DIR):
        for fn in filenames:
            if fn != "SKILL.md":
                continue
            path = Path(dirpath) / fn
            rel = path.relative_to(ROOT)
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            fm = parse_frontmatter(lines[:50])
            name = fm.get("name") or path.parent.name
            description = fm.get("description", "").strip('"')
            keywords = []
            if "keywords" in fm:
                keywords = normalize_keywords(fm["keywords"])
            skills.append({
                "name": name,
                "description": description,
                "keywords": keywords,
                "path": str(rel),
            })

    # write keyword ledger
    ledger_csv = OUT_DIR / "keyword_ledger.csv"
    with open(ledger_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["skill", "keywords"])
        for s in sorted(skills, key=lambda x: x['name'].lower()):
            writer.writerow([s["name"], ";".join(s["keywords"])])

    # write skills_index.csv
    skills_index = OUT_DIR / "skills_index.csv"
    with open(skills_index, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "description", "keywords", "path"])
        for s in sorted(skills, key=lambda x: x['name'].lower()):
            writer.writerow([s["name"], s["description"], ";".join(s["keywords"]), s["path"]])

    # concatenate all SKILL.md into mcp
    mcp_path = ROOT / "mcp"
    with open(mcp_path, "w", encoding="utf-8") as out:
        for s in sorted(skills, key=lambda x: x['name'].lower()):
            p = ROOT / s["path"]
            out.write(f"# Skill: {s['name']}\n")
            out.write(f"Source: {s['path']}\n\n")
            with open(p, "r", encoding="utf-8") as f:
                out.write(f.read())
                out.write("\n\n---\n\n")

    print("Wrote:", ledger_csv, skills_index, mcp_path)


if __name__ == "__main__":
    main()
