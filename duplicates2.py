import pandas as pd

csv_file_path = "./data/words_for_email.csv"
txt_path = "data/new_vocab.txt"

# Load CSV
df = pd.read_csv(csv_file_path, encoding="utf-8-sig")

excel_words = set(df["word"].dropna().astype(str).str.strip().str.lower())

# Load words from text file
with open(txt_path, "r") as txt_file:
    txt_words = set(line.strip().lower() for line in txt_file if line.strip())

# Find matches
matches = txt_words & excel_words

# Output results
print(f"Found {len(matches)} matches:")
for word in sorted(matches):
    print(f" - {word}")