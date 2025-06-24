import json
from pathlib import Path

# Load listings.json
with open('.github/scripts/listings.json', 'r') as f:
    listings = json.load(f)

# Sort (optional)
listings = [x for x in listings if x.get("company")]  # Remove items with no company
listings.sort(key=lambda x: x["company"].lower())

# Generate markdown
table_header = "| Company | Role | Location | Link |\n|---------|------|----------|------|\n"
table_rows = [
    f"| {entry['company']} | {entry['role']} | {entry['location']} | [Apply Here]({entry['link']}) |"
    for entry in listings
]
table = table_header + "\n".join(table_rows)

# Template README
readme_path = Path("README.md")
if readme_path.exists():
    readme_content = readme_path.read_text()
else:
    readme_content = "# Summer 2026 Internships\n\nBelow is a list of internship listings.\n\n<!-- START_TABLE -->\n\n<!-- END_TABLE -->"

# Replace between markers
new_readme = []
inside_table = False
for line in readme_content.splitlines():
    if "<!-- START_TABLE -->" in line:
        new_readme.append(line)
        new_readme.append(table)
        inside_table = True
    elif "<!-- END_TABLE -->" in line:
        inside_table = False
        new_readme.append(line)
    elif not inside_table:
        new_readme.append(line)

# Write back
readme_path.write_text("\n".join(new_readme) + "\n")
