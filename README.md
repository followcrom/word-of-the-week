# W.O.W.

**Word of the Week** is designed to enrich vocabulary through weekly engagement. A Python script selects an esoteric word from a CSV file. This word, along with its definition and a contextual example sentence, is then emailed to a list of recipients.  GitHub Actions automates the delivery process, ensuring the email arrives reliably at a predetermined time each week.

📩 [Subscribe to recieve a word of the week](https://www.followcrom.online/wotd/).

👨🏻‍💻 For the story behind the project, [read the blog post](https://medium.com/@followcrom/books-bytes-and-daily-insights-c22a4e169b10).

📚 See a selection of the [books that have contributed to Word of the Week](https://www.followcrom.online/wotd/books_list.html).

<div align="center">
  <img src="https://www.followcrom.online/images/wordOftheDay.png" width="400">
</div>

## How to Use

Activate the virtual environment:

`source wow_venv/bin/activate`

## Add New Words

1. Copy new words from 'new_vocab.txt' to 'new_words_list.csv'. **Note**: Keep the column headers in the csv file.

2. Run `new_words_list.py` to populate the csv with word types, definitions, and example sentences.

3. Check the csv file for any errors.

4. Manually copy & paste from 'new_words_list.csv' to 'words_for_email.csv'.

5. To sort 'words_for_email.csv' in Excel: Select all -> Sort & Filter -> Custom Sort -> Sort by 'word' -> A to Z. **Note**: Be sure to check _My data has headers_. This ensures that Excel recognizes the first row as headers and excludes it from the sort.

<br>

## Test workflow locally

To send an email to just one person, run `wow_dev.py`. This requires the `python-dotenv` package to access the environment variables in the `.env` file. This is not required for the GitHub Actions workflow as that uses GitHub Secrets.

**Note**: If you have a .env file in your project directory and the Python extension installed, VS Code automatically loads these variables into terminals it opens. This is not the case in terminals outside of VS Code. (Is this true? 🤔 I can run the scripts in Ubuntu 🐧.) 🧐

## Test workflow on GitHub

1. Make sure the workflow YAML file includes the 'workflow_dispatch' trigger.

2. Under the 'Actions' tab, select the Workflow in the left sidebar.

3. Click the 'Run workflow' button on the right side of the workflow page.

4. Start the Workflow: Click 'Run workflow' again in the dropdown menu that appears.

<br>

## Local data

Check for duplicates in 'words_for_email.csv' by running `duplicates.py`.

Create the alphabetized 'Word_List' XL Worksheet by running `alphabetize.py`. This creates a new file every time it is run. **Note the encoding**; some entries have been removed if they have accents (e.g, éclat).

## Updates

Get the latest word count by running `duplicates.py`.

- Word count for 07/10/24: 559
- Word count for 05/06/24: 556
- Word count for 23/04/24: 537
- Word count for 22/04/24: 532

<br>

## Troubleshooting & Support 👨‍🔧

### Gmail SMTP Error 🛠️

On changing my Gmail password, the Python script was no longer able to send emails. The error message was:

```
Failed to send email: (535, b'5.7.8 Username and Password not accepted. …')
```

Google does not allow you to log in via smtplib because it has flagged this as "Less secure app access". To resolve this, you need to generate an app password.

- Log into your Google account and go to the following link: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

- Create a new app password. Type a name for the password and click 'Create'. This will generate a 16-character password.

- The app password for this project is **_wow_**.

- In the `.env` file, use the new app password as **GMAIL_PASSWORD**.

<br>

### Allow VS Code Through UFW 🤖

If ufw is active, you need to allow connections on the ports used by VS Code. By default, VS Code uses port 22 for SSH and some random ports for its server. Here are the steps to allow those ports:

1. Allow SSH:

```sh
sudo ufw allow 22/tcp
```

2. Allow High-Numbered Port Range (to cover dynamically assigned ports):

```sh
sudo ufw allow 30000:65535/tcp
```


#### Identifying the Ports Used by VS Code 🔬

**Remote - WSL** typically uses dynamically assigned ports. However, you can check the VS Code Remote Server Logs to identify and allow only the required ports:

- Open the Command Palette (Ctrl+Shift+P).
- Type and select `Remote-WSL: Show Log`.
- Look for the line that says _"Remote server listening on"_ followed by a port number. This is the port used by the VS Code server.
- You can also find this under `View -> Output -> Ports`.

```sh
# Allow Specific Ports:
sudo ufw allow 60713/tcp
sudo ufw allow 49893/tcp

# Allow Localhost Connections (optional but useful for internal traffic):
sudo ufw allow from 127.0.0.1

# Reload UFW:
sudo ufw reload

# Verify UFW Rules:
sudo ufw status numbered

# Re-enable ufw if it was disabled
sudo ufw enable
```

<br>

### Copilot 🧑‍🚀

`ctrl + enter` to get Copilot suggestions.

## Contact

🌐 followCrom: [followcrom.online](https://followcrom.online/index.html) 🌐

📫 followCrom: [get in touch](https://followcrom.online/contact/contact.php) 📫

## Contributing

👷 Feel free to open a pull request or branch from this project. 👷

## License

This project is open source and available under the MIT License.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)