import pandas as pd

csv_file_path = "./data/words_for_email.csv"
txt_path = "data/new_vocab.txt"

# Load CSV
df = pd.read_csv(csv_file_path, encoding="utf-8-sig")

# Read words from TXT file (skip comments and blank lines)
with open(txt_path, "r") as txt_file:
    words = set(
        line.strip()
        for line in txt_file
        if line.strip() and not line.startswith("!")
    )

# Filter rows where 'word' is in the words set
matches = df[df['word'].isin(words)]

# Print matching rows
if not matches.empty:
    print(matches)
else:
    print("No matches found.")