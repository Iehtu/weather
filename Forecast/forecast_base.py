import datetime
import requests


class ForecastBase(object):
    temp_day: int
    temp_night: int
    wind_direction: str
    wind_speed: int
    condition: str
    date: datetime.datetime

    def __init__(self, date, temp_day, temp_night, wind_speed, wind_direction, condition):
        self.temp_day = temp_day
        self.temp_night = temp_night
        self.date = date
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.condition = condition

    def __repr__(self):
        return f'{self.date}:{self.condition} Температура ночью: {self.temp_night}, днем: {self.temp_day}'

class Forecaster(object):
    href = ''
    result = None
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
