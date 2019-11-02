import requests
from datetime import datetime

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
            print(outage_date)
            if (datetime.now() - outage_date).days < 30:
                return f'Recent outage on {outage_date.strftime(date_format)} UTC'
                
        return 'No recent outages.'

# test
outages = OutageAPI()
city = input()
city = city.title()
print(outages.get_data(city))
