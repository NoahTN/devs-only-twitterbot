
from waqi_python import client as base

class WeatherAPI:
    def __init__(self):
        self.client = base.WaqiClient()
        self.my_station = self.client.get_local_station()
  
    def get_aqi(self, city):
        self.my_station.city.name = city
        value = self.my_station.aqi
        quality = ""

        if value < 50: #0-50
            quality = 'Good'
        elif 50 < value < 101: #51-100
            quality = 'Moderate'
        elif 100 < value < 151: #101-150
            quality = 'Unhealthy for sensitive people'
        elif 150 < value < 201: #151-200
            quality = 'Unhealthy'
        elif 200 < value < 301: #201-300
            quality = 'Very Unhealthy'
        else:
            quality = 'Hazardous'

        return f'Your Air Quality is: {quality}'
        
wapi = WeatherAPI()
print(wapi.get_aqi("Monterey"))
