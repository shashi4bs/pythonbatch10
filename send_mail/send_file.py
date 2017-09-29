# import the smtplib module. It should be included in Python by default
import smtplib
from credz import MY_ADDRESS,PASSWORD
# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=465)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
