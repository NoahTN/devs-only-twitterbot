import requests
import json

class OutageAPI:
    # get multiple
    def get_data(self, city):
        # makes request
        json_data = requests.get('https://pge-outages.simonwillison.net/pge-outages/outages.json?_labels=on').json()
        region_set = {}
        for i in range(len(json_data["rows"])):
            region_set[json_data["rows"][i]["regionName"]["label"]] = i
        if city in region_set:
            print(json_data["rows"][region_set.get(city)])
        else:
            print("No outages in your city!")

# test
outages = OutageAPI()
city = input()
outages.get_data(city)