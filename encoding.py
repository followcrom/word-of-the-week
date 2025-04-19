import pandas as pd
import chardet

input_path = "./data/words_for_email.csv"
output_path = "./data/words_for_email_2.csv"


with open(input_path, "rb") as f:
    raw_data = f.read()
    detected = chardet.detect(raw_data)
    source_encoding = detected["encoding"]
    print(f"Detected encoding: {source_encoding}")


# Re-encode while logging changes
with open(input_path, "r", encoding=source_encoding, errors="replace") as source_file:
    with open(output_path, "w", encoding="utf-8-sig", errors="replace") as target_file:
        for i, line in enumerate(source_file, 1):
            # Store original and replacement markers
            if "�" in line:
                print(f"Line {i} had undecodable characters. Replaced with �:")
                print(f"  {line.strip()}")
            target_file.write(line)