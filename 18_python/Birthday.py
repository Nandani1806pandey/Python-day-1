from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "nandani1806pandey@email.com"
MY_PASSWORD = "N@nd@nipnadey181071"

today = datetime.now()
today_tuple = (today.month, today.day)
date = pandas.read_csv(r"c:/Users/pande/OneDrive/Desktop/nandani/Python/18_python/birthday.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in date.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"c:/Users/pande/OneDrive/Desktop/nandani/Python/18_python/letter_template/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[Name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs = birthday_person["email"],
            msg = f"Subject:Happy Birthday!\n\n{contents}"
        )