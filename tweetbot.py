# importing the module 
import tweepy 
import json
import urllib.request
import requests
from datetime import datetime
from pytz import timezone
import pytz
from weather import Weatherapi
from outage import OutageAPI
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
api.update_with_media('chunger.png',status =f"{weather_data}\n\
Outages: \n\
{outage_data}. \n\
Traffic incidents: \n\
{traffic_data}")
