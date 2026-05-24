import pandas as pd

csv_file_path = "./data/words_for_email.csv"
txt_path = "data/new_vocab.txt"

# Load CSV
df = pd.read_csv(csv_file_path, encoding="utf-8-sig")

# Normalised lookup column for case/whitespace-insensitive matching
df["_word_key"] = df["word"].dropna().astype(str).str.strip().str.lower()

# Read words from TXT file (skip blank lines and ! comments), normalised
with open(txt_path, "r") as txt_file:
    words = set(
        line.strip().lower()
        for line in txt_file
        if line.strip() and not line.startswith("!")
    )

# Filter rows where the normalised word is in the txt word set
matches = df[df["_word_key"].isin(words)][["word", "word_type"]]

if matches.empty:
    print("No matches found.")
else:
    print(f"Found {len(matches)} matching row(s):\n")
    print(matches.to_string(index=False))
