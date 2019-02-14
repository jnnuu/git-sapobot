import requests
import json
from datetime import datetime
import sys

global city
kokoviesti = []		# Results of the request are saved this list
appId = '' 		# Register on openweathermap and enter your appid here

def makeRequest(city):	# You need to register in openweathermap.org to use this API
	r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&APPID=' + appId  +  '&units=metric')
	global json_object
	json_object = r.json()
	kokoviesti.append('{0}:'.format(city))	# City name is the first row of the weather forecast document
	printResults(city) 			# Calling the printResults function below

def printResults(city):
	print("Weather forecast for {0}:".format(city))

	for x in range(0,20):
		aikaunix = int(json_object['list'][x]['dt'])
		klo = int(datetime.utcfromtimestamp(aikaunix).strftime('%H'))
		lampo = int(json_object['list'][x]['main']['temp'])
		kuvaus = json_object['list'][x]['weather'][0]['description']
		aikahuman = datetime.utcfromtimestamp(aikaunix).strftime('%d.%m hour: %H')
		rivi = ('{0} : {1} *C : {2}'.format(aikahuman, lampo, kuvaus))
		if (klo == 00):		# Day changed, formatting....
			kokoviesti.append('-------------------------')
			kokoviesti.append(rivi)
		else:
			print(rivi)	# Printing the results in console
			kokoviesti.append(rivi)
