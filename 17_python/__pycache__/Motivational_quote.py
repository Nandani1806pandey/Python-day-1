import smtplib
import datetime as dt
import random

MY_EMAIL = "nandani1806pandey@gmail.com"
MY_PASSWORD = "N@nd@ni1806pandey"

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt", encoding="utf-8") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

print(f"Today's quote: {quote}")

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs = MY_EMAIL, 
            msg = f"Subject: Monday Motivation \n\n{quote}")