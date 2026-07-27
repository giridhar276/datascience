from pathlib import Path

file_path = Path("sample_notes.txt")
file_path.write_text("Python\nFile Handling\nContext Managers\n", encoding="utf-8")
content = file_path.read_text(encoding="utf-8")
print(content)
