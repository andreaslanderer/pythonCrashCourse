from pathlib import Path

path = Path("learning_python.txt")
content = path.read_text()
lines = content.splitlines()

for line in lines:
    modified_line = line.replace("Python", "Kotlin")
    print(modified_line)
    