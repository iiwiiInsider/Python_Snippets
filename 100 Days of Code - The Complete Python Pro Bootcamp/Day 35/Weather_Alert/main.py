import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "c1c85c57e69ecbf21239624a79e585b6"


weather_params = {
    "lat": -33.781890,
    "lon": 18.478406,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

    if will_rain:
        print("Have with you an umbrella. It might rain today.")

