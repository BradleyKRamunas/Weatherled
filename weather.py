import requests
import json
import pprint
from weather_provider import WeatherProvider
from weather_condition import WeatherCondition
from mock_weather_provider import MockWeatherProvider

weather_provider = MockWeatherProvider()
print(weather_provider.get_current_weather())