import requests
import json
from datetime import datetime
import sys
from pprint import pprint


appId = ''

global city
kokoviesti = [] #Results of the request are saved this list


def makeRequest(city):
	r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&APPID=' + appId + '&units=metric')
	global json_object
	json_object = r.json()
	kokoviesti.append('{0}:'.format(city))
	printResults(city)

def printResults(city):
	print("Weather forecast for {0}:".format(city))

	for x in range(0,20):
		aikaunix = int(json_object['list'][x]['dt'])
		klo = int(datetime.utcfromtimestamp(aikaunix).strftime('%H'))
		lampo = int(json_object['list'][x]['main']['temp'])
		kuvaus = json_object['list'][x]['weather'][0]['description']
		tuuli = int(json_object['list'][x]['wind']['speed'])
		aikahuman = datetime.utcfromtimestamp(aikaunix).strftime('%d.%m hour: %H')
		rivi = ('{0} : {1} *C : {2}, wind: {3} m/s'.format(aikahuman, lampo, kuvaus, tuuli))
		if (klo == 00): #Day changed, formatting....
			kokoviesti.append('-------------------------')
			print('-------------------------')
			kokoviesti.append(rivi)
		else:
			print(rivi)
			kokoviesti.append(rivi)
