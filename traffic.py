import requests
import json

class TrafficAPI:
    # get multiple
    def get_data(self):
        # makes request
        json_data = requests.get('http://www.mapquestapi.com/traffic/v2/incidents?key=MfFt1rJi4T1sJLHkfIaITmfEzMdO57HM&boundingBox=36.44,121.4,36.34,122.56&filters=construction,inciden').json()
        print(json_data)
        
        region_set = {}
        for i in range(len(json_data["rows"])):
            region_set[json_data["rows"][i]["regionName"]["label"]] = i
        if city in region_set:
            yes = json_data["rows"][region_set.get(city)]
            return yes;
        else:
            no = "No outages in your city!"
            return no;

# test
traffic = TrafficAPI()
traffic.get_data()
