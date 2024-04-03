import smtplib

MY_EMAIL = "lambdaa112@gmail.com"
TARGET_EMAIL = "kamazim121212@gmail.com"
PASSWORD = "ynha ervn pgwy cink"

connection = smtplib.SMTP("smtp.gmail.com") # A way to connect to our email providers smtp email server
connection.starttls() # Stands for transport layer security and is a way of securing our connection to an email server
connection.login(user=MY_EMAIL, password = PASSWORD) 
connection.sendmail(from_addr=MY_EMAIL, to_addrs=TARGET_EMAIL, msg = "Subject:Hello\n\nThis is the body of my email.") 
connection.close()