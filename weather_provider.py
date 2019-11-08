import requests
import json
from weather_condition import WeatherCondition

class WeatherProvider:
    def __init__(self, url='https://api.weather.gov/gridpoints/MTR/93,109/forecast'):
        self.api_url = url

    def get_current_weather(self):
        '''
        Gets the current weather condition by accessing the weather api at api_url.

        Returns a tuple of (WeatherCondition, temperature in fahrenheit)
        '''
        response = requests.get(self.api_url)
        if response.status_code == 200:
            # STATUS_CODE OK (200)
            response_obj = json.loads(response.content)
            weather_period = response_obj['properties']['periods'][0]
            return (self.convert_shortforecast(weather_period['shortForecast']), weather_period['temperature'])
        else:
            # STATUS_CODE NOT OK (!200)
            return (WeatherCondition.UNKNOWN, 0)

    def convert_shortforecast(self, forecast):
        lower_forecast = forecast.lower()
        if 'thunderstorms' in lower_forecast or 'storms' in lower_forecast:
            return WeatherCondition.THUNDERSTORMS
        if 'cloudy' in lower_forecast or 'cloudy' in lower_forecast:
            return WeatherCondition.CLOUDY
        if 'clear' in lower_forecast:
            return WeatherCondition.CLEAR
        if 'sunny' in lower_forecast or 'sun' in lower_forecast:
            return WeatherCondition.SUNNY
        if 'rain' in lower_forecast or 'rainy' in lower_forecast:
            return WeatherCondition.RAINY
        if 'showers' in lower_forecast or 'shower' in lower_forecast:
            return WeatherCondition.SHOWERS
        return WeatherCondition.UNKNOWN
