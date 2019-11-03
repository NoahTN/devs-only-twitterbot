import requests
import json

class TrafficAPI:
    # get multiple
    def get_data(self):
        # makes request
        json_data = requests.get('http://www.mapquestapi.com/traffic/v2/incidents?key=MfFt1rJi4T1sJLHkfIaITmfEzMdO57HM&boundingBox=36.74,-121.99,36.5,-121.59&filters=construction,incidents').json()
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
            masterString = ""
            for x in range(min(len(shortDesc), 2)):
                masterString += shortDesc[x]
                masterString += "\n"
        return masterString
