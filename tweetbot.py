# importing the module 
import tweepy 
import json
import urllib.request
import requests
from datetime import datetime
 
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
  
#weather api 

loca=""
url='http://api.openweathermap.org/data/2.5/weather?q=monterey,us&appid=c9ed41a4f7c70f576c1527b42d197266    '

with urllib.request.urlopen(url) as url:
    s = url.read()

j = json.loads(s)
main = j["main"]
temp = main["temp"]
tmp = int(round(temp-273))

main = j["main"]
temp = main["temp"]

weather = j["weather"]
temp1 = weather[0]
main = temp1["main"]
condition = temp1["description"]

sys = j['sys']
country= sys['country']

name = j['name']

#outage
class OutageAPI:
    # get multiple
    def get_data(self, city):
        # makes request
        json_data = requests.get('https://pge-outages.simonwillison.net/pge-outages/outages.json?_labels=on').json()
        region_set = {}
        for i in range(len(json_data["rows"])):
            region_set[json_data["rows"][i]["regionName"]["label"]] = i
        if city in region_set:
            yes = json_data["rows"][region_set.get(city)]
            return yes;
        else:
            no = "No outages in your city!"
            return no;

outages = OutageAPI()

a = outages.get_data('Monterey')


class TrafficAPI:
    # get multiple
    def get_data(self):
        # makes request
        json_data = requests.get('http://www.mapquestapi.com/traffic/v2/incidents?key=MfFt1rJi4T1sJLHkfIaITmfEzMdO57HM&boundingBox=39.95,-105.25,39.52,-104.71&filters=construction,incidents').json()
        incidents = json_data["incidents"]
        shortDesc = []
        for i in incidents:
            #print(i)
            if i["type"]  > 2 :
                shortDesc.append(i["shortDesc"])
                #print(i["shortDesc"])
        #print(json_data)
        if len(shortDesc) == 0:
            masterString = "The roads look clear"
        else:
            for x in range(2):
                masterString += shortDesc[x]
                masterString += "\n"
        return masterString
        

# test
traffic = TrafficAPI()
traffic.get_data()
#^^^ not added to tweet bot as of the current




#update status of monterey
api.update_with_media('chunger.png',status =f"{name}, {country}.\n\
{temp}ºF. Condition: {condition}.\n\
Outages: {a}. \n ")
