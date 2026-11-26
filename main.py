"""One-Liner Laughs — entry for make.fun.

Writes one funny line to /output/entry.txt.
"""
import os

# The joke: the plants get revenge — tell them you're on vacation and they start watering you with guilt instead.
TEXT = "I told my plants I'm taking a vacation — now they're the ones watering me with guilt."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
