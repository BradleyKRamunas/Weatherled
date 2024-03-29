import requests
import json
import time
from weather_provider import WeatherProvider
from weather_condition import WeatherCondition
from mock_weather_provider import MockWeatherProvider
from bitmaps import convert_condition_to_bitmap, convert_temperature_to_bitmap
from serial_write import SerialWriter

weather_provider = MockWeatherProvider()
condition, temp = weather_provider.get_current_weather()
print(condition, temp)
serial_writer = SerialWriter('/dev/ttyS4')
serial_writer.write(convert_temperature_to_bitmap(temp))
serial_writer.write(convert_condition_to_bitmap(condition))
