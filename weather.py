import requests
import json
# -1.1078422427578574, 37.01383246479483
weather_url ="https://api.openweathermap.org/data/2.5/weather"
weather_parameters = {
    "lat":-1.1078422427578574,
    "lon":37.01383246479483,
    "appid":"2c3b43ed8321f5227ae73d31e3418439"
}
weather_response=requests.get(weather_url,weather_parameters)
parsed_data=(weather_response.json())
print(json.dumps(parsed_data,indent=4))


# print(weather_response.json)