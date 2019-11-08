import random
from weather_condition import WeatherCondition

class MockWeatherProvider:
    def __init__(self):
        self.conditions = [WeatherCondition.UNKNOWN, WeatherCondition.CLEAR, WeatherCondition.CLOUDY,
        WeatherCondition.SHOWERS, WeatherCondition.SUNNY, WeatherCondition.THUNDERSTORMS, WeatherCondition.RAINY]

    def get_current_weather(self):
        '''
        Mocks the current weather using randomly generated values.

        Returns a tuple of (WeatherCondition, temperature in fahrenheit)
        '''
        return (random.choice(self.conditions), random.randint(0, 99))