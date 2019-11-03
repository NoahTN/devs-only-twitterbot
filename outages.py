import requests
from datetime import datetime
from pytz import timezone
import pytz

class OutageAPI:

    def get_data(self, city):
        json_data = requests.get(f'https://pge-outages.simonwillison.net/pge-outages.json?sql=select+%2A+from+outages_expanded+where+%22min_estCustAffected%22+%3E+%3Ap0+and+%22region%22+%3D+%3Ap1+order+by+earliest+desc+limit+1&p0=9&p1={city}').json()

        if len(json_data['rows']) == 1:
            date_format='%A, %B %d at %I:%M %p'
            outage_date = datetime.fromtimestamp(json_data['rows'][0][1])
            if (datetime.now() - outage_date).days < 30:
                outage_date = outage_date.astimezone(timezone('US/Pacific'))
                return f'Recent outage on {outage_date.strftime(date_format)} PT'
                
        return 'No recent outages.'

# test
outages = OutageAPI()
city = input()
city = city.title()
print(outages.get_data(city))
