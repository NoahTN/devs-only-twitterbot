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
    def __init__(self):
        self.region_codes = {}
        # should performed only once
        regions = requests.get('https://pge-outages.simonwillison.net/pge-outages.json?sql=select+*+from+regionName').json()
        for region in regions["rows"]:
            self.region_codes[region[1]] = region[0]

    def get_data(self, city):
        if city not in self.region_codes:
            return 'Untracked city.'
        
        region_code = self.region_codes[city]

        json_data = requests.get(f'https://pge-outages.simonwillison.net/pge-outages.json?sql=select+*+from+outages+where+%22regionName%22+%3D+%3Ap0+order+by+outageStartTime+desc+limit+1&p0={region_code}').json()

        if len(json_data['rows']) == 1:
            date_format='%A, %B %d at %I:%M %p'
            outage_date = datetime.fromtimestamp(json_data['rows'][0][1])
            if (datetime.now() - outage_date).days < 30:
                return f'Recent outage on {outage_date.strftime(date_format)} UTC'
                
        return 'No recent outages.'

# test
outages = OutageAPI()
city = 'monterey'
city = city.title()

a = outages.get_data(city)


class TrafficAPI:
    # get multiple
    def get_data(self):
        # makes request
        json_data = requests.get('http://www.mapquestapi.com/traffic/v2/incidents?key=MfFt1rJi4T1sJLHkfIaITmfEzMdO57HM&boundingBox=36.44,121.4,36.34,122.56&filters=construction,inciden').json()
        print(json_data)

# test
traffic = TrafficAPI()
#traffic.get_data()




#update status of monterey
api.update_with_media('chunger.png',status =f"{name}, {country}.\n\
{temp}ºF. Condition: {condition}.\n\
Outages: {a}. \n ")
