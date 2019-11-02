import json
import urllib.request

a = input()

a = a.replace(" ", "%20")

loca=""
url='http://api.openweathermap.org/data/2.5/weather?q='+a+',us&appid={{apikey}}'

with urllib.request.urlopen(url) as url:
    s = url.read()

j = json.loads(s)
main = j["main"]
temp = main["temp"]
tmp = int(round(temp-273))
print(tmp)

main = j["main"]
temp = main["temp"]
print(temp)

weather = j["weather"]
temp = weather[0]
main = temp["main"]
description = temp["description"]
print(main)
print(description)

sys = j['sys']
country= sys['country']
print(country)

name = j['name']
print(name)

