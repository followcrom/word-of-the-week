# W.O.W.

**Word of the Week** uses a Python script to select a random word from a CSV file. That word, along with its definition and example sentences, are emailed to a list of recipients. Using GitHub Actions, the email lands in their inboxes at a scheduled time.

<div align="center">
  <img src="https://www.followcrom.online/embeds/wotd.png" width="400">
</div>

## How to Use

`source wow_venv/bin/activate`

1. Copy new words from new_vocab.txt to new_words_list.csv. **Note**: Keep the column headers.

2. Run new_words_list.py to populate the new words list with word types, definitions, and example sentences.

3. Check the new_words_list.csv file for any errors.

4. Manually copy & paste from new_words_list.csv to completed_words.csv.

5. To sort completed_words.csv in Excel: Select all -> Sort & Filter -> Custom Sort -> sort by 'word' -> A to Z. **Note**: Be sure to check _My data has headers_. This ensures that Excel recognizes the first row as headers and excludes it from the sort criteria.

## Test

To send an email to just one person, run wow_dev.py

## Data

Create the Alphabetized_Word_List XL Worksheet, run working.py. Note the encoding; some entries have been removed if they have accents (éclat).

## Updates

- Word count for 23/04/24: 539

- Word count for 22/04/24: 532