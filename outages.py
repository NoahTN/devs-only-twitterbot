import requests
from datetime import datetime

class OutageAPI:
    def __init__(self):
        self.coords = []
        self.outage_cities = set()

    def get_data(self, city):
        json_data = requests.get(f'https://pge-outages.simonwillison.net/pge-outages.json?sql=select+%2A+from+outages_expanded+where+%22min_estCustAffected%22+%3E+%3Ap0+and+%22region%22+%3D+%3Ap1+order+by+earliest+desc+limit+7&p0=9&p1={city}').json()
        if len(json_data['rows']) != 0:
            for outage in json_data['rows']:
                day_diff = datetime.now() - datetime.fromtimestamp(outage[1])
                if day_diff.days < 3:
                    self.coords.append([outage[-2],outage[-1]])
                    self.outage_cities.add(city)
        
    def get_all_outages(self):
        if len(self.outage_cities) > 0:
            result = 'Outages in the past 3 days at '
            for i in range(len(self.outage_cities)-1):
                result += f'{self.outage_cities.pop()}, '
            result += f'{self.outage_cities.pop()}'
            return result
      
        return 'No recent outages.'

    def get_coords(self):
        return self.coords