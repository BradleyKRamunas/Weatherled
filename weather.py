import requests
import json
import pprint
from weather_provider import WeatherProvider
from weather_condition import WeatherCondition
from mock_weather_provider import MockWeatherProvider
from bitmaps import convert_condition_to_int, convert_temperature_to_int

weather_provider = MockWeatherProvider()
condition, temp = weather_provider.get_current_weather()
print(condition, temp)
print(convert_condition_to_int(condition), convert_temperature_to_int(temp))