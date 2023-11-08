from pathlib import Path

path = Path("learning_python.txt")
content = path.read_text().strip()
print("File content:")
print(content)

print("\nFile content:")
lines = content.splitlines()
for line in lines:
    print(line)
