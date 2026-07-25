import csv
import smtplib
import random
import datetime

my_email = "kdbburns.social@gmail.com"
password = "vtrv opyv dzhl cbgk"

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

birthdays_dict = {}

with open("birthdays.csv", newline='') as file:
    # Read first line (header)
    raw_header = file.readline().strip()

    # Remove BOM and quotes
    raw_header = raw_header.replace("\ufeff", "")
    raw_header = raw_header.strip('"')

    header = raw_header.split(",")

    # Now read the rest of the file manually
    reader = csv.reader(file)

    for row in reader:
        # If row is quoted as one string, split it
        if len(row) == 1:
            row = row[0].strip('"').split(",")

        # Map row values to header names
        row_dict = dict(zip(header, row))

        # Convert month/day safely
        try:
            month = int(row_dict["month"])
            day = int(row_dict["day"])
        except Exception as e:
            print("Bad row:", row_dict)
            continue

        birthdays_dict[(month, day)] = row_dict

# Check for birthday match
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read().replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

print("Script executed successfully.")
