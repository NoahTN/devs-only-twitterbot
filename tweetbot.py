# importing the module 
import tweepy
import os 
import json
import urllib.request
import requests
from weather import WeatherAPI
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
weather = WeatherAPI()
weather_data = (weather.get_data("Monterey"))

#outage
outages = OutageAPI()
city = 'Monterey'
city = city.title()
locations = ["Salinas", "Monterey", "Marina"]
for loc in locations:
    outages.get_data(loc)

outage_data = outages.get_all_outages()

# Traffic
traffic = TrafficAPI()
traffic_data = traffic.get_data()

# draw map image
map_draw = MapDraw()
filename = "temp.jpg"
response = requests.get(map_draw.get_image_url(outages.get_coords()), stream=True)
os.chdir('/tmp')
with open(filename, 'wb') as image:
    for chunk in response:
        image.write(chunk)
os.chdir('..')

# update status
api.update_with_media(filename,status=f"{weather_data}\n\
Outages: \n\
{outage_data}. \n\
Traffic incidents: \n\
{traffic_data}")
