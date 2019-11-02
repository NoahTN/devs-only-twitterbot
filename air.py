
class WeatherAPI:
    def __init__(self):
        from waqi_python import client as base
        client = base.WaqiClient()
        my_station = client.get_local_station()
        my_station.city.name = 'San Francisco-Arkansas Street, San Francisco, California'
        print(my_station.aqi)


wapi = WeatherAPI()

