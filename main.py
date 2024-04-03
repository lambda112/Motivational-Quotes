import smtplib
from random import randint

MY_EMAIL = "lambdaa112@gmail.com"
TARGET_EMAIL = "kamazim121212@gmail.com"
PASSWORD = "ynha ervn pgwy cink"

# Can use similar to file context manager
with smtplib.SMTP("smtp.gmail.com") as connection: # A way to connect to our email providers smtp email server
    
    # Grabbing Quote
    with open("quotes.txt", "r") as f:
        lines = f.readlines()
        random_num = randint(0,len(lines) - 1)
        quote = lines[random_num].strip()
        del lines[random_num] 

    connection.starttls() # Stands for transport layer security and is a way of securing our connection to an email server
    connection.login(user=MY_EMAIL, password = PASSWORD) 
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=TARGET_EMAIL, msg = f"Subject:Motivational Quote\n\n{quote}\n\nAutomated with Python") 
    # To add subject use colon and then two newlines for content
