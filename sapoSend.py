#-*- coding: utf-8 -*-

import weather
import smtplib, ssl
import time

city = 'Espoo'				 # Enter your city here
port = 465				 # For SSL
smtp_server = "smtp.mail.yahoo.com"	 # For Yahoo emails

receiver_email = ''	 # Enter your destination email here (your main email address?)
sender_email = ''	 # Enter the email what you are using for sending the emails
		 	 # Yahoo works better than gmail in this use imo
password = ''		 # sender_email password for logging into the smtp server


def looper():

	weather.makeRequest(city)		 # Calling the request function in weather.py

	text = '\n'.join(weather.kokoviesti)	 # kokoviesti[] formatted as string
	subject = 'Weather forecast for {}'.format(city)

	message = ('Subject: {}\n\n{}'.format(subject, text))

	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
		print('email sent') 
		server.quit()
	time.sleep(86400)	 #Sleeping for 86400 seconds = 1 day

while (True):
	looper()		 #loop infinitely until cancelled.
