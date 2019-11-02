
from waqi_python import client as base

class WeatherAPI:
    def __init__(self, city):
        client = base.WaqiClient()
        my_station = client.get_local_station()
        my_station.city.name = city
        value = my_station.aqi

        print('Air Quality Index is: ')
        print(my_station.aqi)

        print('Your Air Quality Is: ')

        if value < 50: #0-50
            print ('Good')
        elif 50 < value < 101: #51-100
            print ('Moderate')
        elif 100 < value < 151: #101-150
            print ('Unhealthy for sensitive people')
        elif 150 < value < 201: #151-200
            print ('Unhealthy')
        elif 200 < value < 301: #201-300
            print ('Very Unhealthy')
        elif value > 300: #301+
            print ('Hazardous')

        
wapi = WeatherAPI()

