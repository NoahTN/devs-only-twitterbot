import requests
import json

class TrafficAPI:
    # get multiple
    def get_data(self):
        # makes request
        json_data = requests.get('http://www.mapquestapi.com/traffic/v2/incidents?key=MfFt1rJi4T1sJLHkfIaITmfEzMdO57HM&boundingBox=36.44,121.4,36.34,122.56&filters=construction,inciden').json()
        print(json_data)

# test
traffic = TrafficAPI()
traffic.get_data()
