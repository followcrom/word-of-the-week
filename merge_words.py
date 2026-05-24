import pandas as pd

main_csv_path = "./data/words_for_email.csv"
new_csv_path = "./data/new_words_list.csv"

main_df = pd.read_csv(main_csv_path)
new_df = pd.read_csv(new_csv_path)

combined_df = pd.concat([main_df, new_df], ignore_index=True)
combined_df = combined_df.sort_values(by="word", key=lambda col: col.str.lower()).reset_index(drop=True)

combined_df.to_csv(main_csv_path, index=False)

print(
    f"Added {len(new_df)} rows from {new_csv_path} into {main_csv_path}. "
    f"Total rows now: {len(combined_df)}."
)
