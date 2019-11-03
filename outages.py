import requests
from datetime import datetime
from pytz import timezone
import pytz

class OutageAPI:
    def __init__(self):
        self.coords = []
    
    
    def get_data(self, city):
        json_data = requests.get(f'https://pge-outages.simonwillison.net/pge-outages.json?sql=select+%2A+from+outages_expanded+where+%22min_estCustAffected%22+%3E+%3Ap0+and+%22region%22+%3D+%3Ap1+order+by+earliest+desc+limit+7&p0=9&p1={city}').json()

        if len(json_data['rows']) != 0:
            date_format='%A, %B %d at %I:%M %p'
            outage_date = datetime.fromtimestamp(json_data['rows'][0][1])
            if (datetime.now() - outage_date).days < 3:
                outage_date = outage_date.astimezone(timezone('US/Pacific'))
                return f'Recent outage on {outage_date.strftime(date_format)} PT'
                
        return 'No recent outages.'

    def store_coords(self, city):
        json_data = requests.get(f'https://pge-outages.simonwillison.net/pge-outages.json?sql=select+%2A+from+outages_expanded+where+%22min_estCustAffected%22+%3E+%3Ap0+and+%22region%22+%3D+%3Ap1+order+by+earliest+desc+limit+7&p0=9&p1={city}').json()

        if len(json_data['rows']) != 0:
            for outage in json_data['rows']:
                day_diff = datetime.now() - datetime.fromtimestamp(outage[1])
                if day_diff.days < 3:
                    self.coords.append([outage[-2],outage[-1]])

    def get_coords(self):
        return self.coords