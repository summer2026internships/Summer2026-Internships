import json

start_marker = "<!-- START_TABLE -->"
end_marker = "<!-- END_TABLE -->"

with open(".github/scripts/listings.json") as f:
    data = json.load(f)

table_lines = [
    "| Company | Role | Location | Link |",
    "| --- | --- | --- | --- |",
]

for item in data:
    row = f"| {item.get('company', '')} | {item.get('role', '')} | {item.get('location', '')} | [Apply]({item.get('link', '')}) |"
    table_lines.append(row)

with open("README.md", "r") as f:
    content = f.read()

start_idx = content.find(start_marker) + len(start_marker)
end_idx = content.find(end_marker)

new_content = content[:start_idx] + "\n" + "\n".join(table_lines) + "\n" + content[end_idx:]

with open("README.md", "w") as f:
    f.write(new_content)
