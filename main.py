import smtplib
import datetime as dt
from random import randint
from random import choice

MY_EMAIL = "lambdaa112@gmail.com"
TARGET_EMAIL = "kamazim121212@gmail.com"
PASSWORD = "xxxxx"
names = ["Jessie", "James"]

# Can use similar to file context manager
while True:

    # Checking Date and Time
    if dt.datetime.now().minute == 36:
        
        # Grabbing Quote
        with open("quotes.txt", "r") as f:
            lines = f.readlines()
            random_num = randint(0,len(lines) - 1)
            quote = lines[random_num].strip()
            del lines[random_num] 

        with smtplib.SMTP("smtp.gmail.com") as connection: # A way to connect to our email providers smtp email server
            # Sending Email
            connection.starttls() # Stands for transport layer security and is a way of securing our connection to an email server
            connection.login(user=MY_EMAIL, password = PASSWORD) 
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TARGET_EMAIL, msg = f"Subject:Motivational Quote\n\n{quote}\n\n{choice(names)} from Team Rocket") 
            # To add subject use colon and then two newlines for content
            break
