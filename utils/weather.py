'''Utility for API calls to openweathermap to fetch weather data'''
import requests


DEFAULT_API_KEY = "5f3ccc881aa4f8edee5103c7c2ae8355"


def get_weather_data(location, api_key=DEFAULT_API_KEY):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + location + "&units=metric"
    response = requests.get(complete_url)
   
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        report = data['weather']
        description = report[0]['description']
        cont_id = report[0]['id']
        pressure = main["pressure"]
        windspeed = data["wind"]["speed"]
        return {
            'temperature': temperature,
            'humidity': humidity,
            'description': description,
            'id': cont_id,
            'pressure': pressure,
            'wind_speed': windspeed
        }
    else:
        print("Error in the HTTP request")
        return None  # or raise an exception