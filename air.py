
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
        if value < 50:
            print ('Good')
        elif value > 50 && value < 101:
            print ('Moderate')
        elif value > 100 && value < 151:
            print ('Unhealthy for sensitive people')
        elif value > 150 && value < 201
            print ('Unhealthy')
        elif value > 200 && value < 301:
            print ('Very Unhealthy')
        elif value > 300:
            print ('Hazardous')

        


wapi = WeatherAPI()

