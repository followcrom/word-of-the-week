import pandas as pd
import datetime

# Specify the path to your CSV file
csv_file_path = "./data/words_for_email.csv"

# Load the CSV data into a DataFrame, specifying the encoding
df = pd.read_csv(csv_file_path, encoding="utf-8-sig")

# Length of the DataFrame before removing duplicates
print("Length of CSV before removing duplicates:", len(df))

# keep=False will mark all duplicates as True, allowing us to see all versions
duplicate_words = df[df.duplicated(subset=['word', 'word_type'], keep=False)]

# Sort the DataFrame by the 'word' column to better visualize duplicates
sorted_duplicates = duplicate_words.sort_values(by=['word', 'word_type'])

print("No. of duplicates:", len(sorted_duplicates), end="\n\n")

if not sorted_duplicates.empty:
    print(sorted_duplicates)
else:
    print("No duplicates found.")

# Remove duplicates from the DataFrame
df = df.drop_duplicates(subset=['word', 'word_type'], keep='first')

# Length of the DataFrame after removing duplicates
num_unique_words = len(df)

# Get the current date
current_date = datetime.date.today()

print(f"Word count for {current_date.strftime('%d/%m/%y')}: {num_unique_words}")
