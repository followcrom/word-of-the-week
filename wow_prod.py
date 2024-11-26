import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

words_df = pd.read_csv("./data/words_for_email.csv")

# Get a random word and its details
def get_word_of_the_day(df):
    return df.sample().iloc[0]


# Function to format word details, omitting any NaN values
def format_word_details(word_row):
    with open('email_template.html', 'r') as file:
        template = file.read()
    
    formatted_html = template.format(
        word=word_row['word'].upper(),
        word_type=word_row['word_type'],
        definition=word_row['definition'] if not pd.isna(word_row["definition"]) else "Not available",
        examples=word_row['examples'] if not pd.isna(word_row["examples"]) else "Not available"
    )
    
    return formatted_html


def send_email(word_details):
    fromaddr = os.getenv("GMAIL_ACCOUNT")
    toaddr = [email.strip() for email in os.getenv("EMAIL_LIST").split(",")]
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(fromaddr, os.getenv("GMAIL_PASSWORD"))
            
            # Send individual personalized emails
            for recipient in toaddr:
                msg = MIMEMultipart()
                msg["From"] = f"LEXicon John"
                msg["To"] = recipient
                msg["Subject"] = "Word of the Week"
                
                # Attach the message body
                msg.attach(MIMEText(word_details, "html"))
                
                # Send email to each recipient individually
                server.send_message(msg)
                print(f"Email sent to {recipient}")
        
        print(f"Total emails sent: {len(toaddr)}")
    
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Check your email and password")
    except smtplib.SMTPServerDisconnected:
        print("SMTP Server Disconnected: Check your internet connection")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


def main():
    try:
        words_df = pd.read_csv("./data/words_for_email.csv")
        word_of_the_day = get_word_of_the_day(words_df)
        word_details = format_word_details(word_of_the_day)
        send_email(word_details)
    except FileNotFoundError:
        print("Error: CSV file not found.")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
