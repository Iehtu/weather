import datetime
import requests


class ForecastBase(object):
    temp: int
    wind_direction: str
    wind_speed: int
    date: datetime.datetime

    def __init__(self, date, temp, wind_speed, wind_direction):
        self.temp = temp
        self.date = date
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction


class Forecaster(object):
    href = ''
    result = []
    session = None

    def __init__(self):
        self.session = requests.Session()

    def __del__(self):
        if self.session is not None:
            self.session.close()

    def get_forecast(self, town_id: int, date: datetime):
        result = self.session.get(self.href.format(town_id=town_id))
        self.parse_result(result.text)

    def parse_result(self, result):
        return None

    def get_result(self):
        return self.result
