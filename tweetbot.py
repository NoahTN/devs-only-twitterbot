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
from map_draw import MapDraw

 
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
outages.store_coords("Salinas")
outages.store_coords("Monterey")
outages.store_coords("Marina")
outage_data = outages.get_data(city)

# Traffic
traffic = TrafficAPI()
traffic_data = traffic.get_data()

# draw map image
map_draw = MapDraw()
filename = "temp.jpg"
response = requests.get(map_draw.get_image_url(outages.get_coords()), stream=True)
with open(filename, 'wb') as image:
    for chunk in response:
        image.write(chunk)

# update status
api.update_with_media(filename,status=f"{weather_data}\n\
Outages: \n\
{outage_data}. \n\
Traffic incidents: \n\
{traffic_data}")
os.remove(filename)
