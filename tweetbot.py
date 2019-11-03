# importing the module 
import tweepy
import os 
import json
import urllib.request
import requests
from datetime import datetime
from pytz import timezone
import pytz
from weather import Weatherapi
from outages import OutageAPI
from traffic import TrafficAPI

 
# personal details 
consumer_key ="ru5kZBYn4bBnO1hMGYRJKsr11"
consumer_secret ="UjZ6G7PXm2GPLcjNzqCClwjlhMu1mKsA72sHmDaC0wcDF2UOkI"
access_token ="1190661254974590976-OAEU10a7qpNr67ysRWqj2UdvGEqxaA"
access_token_secret ="R47JeIAgB6xyuwowsupGjMHZ1P6KacQMA7gCo0owVRjS1"
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
#weather
weather = Weatherapi()
weather_data = (weather.get_data("Monterey"))


#outage
outages = OutageAPI()
city = 'Monterey'
city = city.title()
outage_data = outages.get_data(city)


# Traffic
traffic = TrafficAPI()
traffic_data = traffic.get_data()


#update status of monterey
filename = "temp.jpg"
response = requests.get('https://www.mapquestapi.com/staticmap/v5/map?boundingBox=36.74,-121.99,36.5,-121.59&zoom=11&traffic=flow|cons|inc&size=700,500@2x&key=MfFt1rJi4T1sJLHkfIaITmfEzMdO57HM', stream=True)
with open(filename, 'wb') as image:
    for chunk in response:
        image.write(chunk)
api.update_with_media('temp.jpg',status =f"{weather_data}\n\
Outages: \n\
{outage_data}. \n\
Traffic incidents: \n\
{traffic_data}")
os.remove(filename)
