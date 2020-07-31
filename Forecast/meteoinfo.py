import datetime
from bs4 import BeautifulSoup
import re

from Forecast.forecast_base import ForecastBase, Forecaster

class Meteoinfo(Forecaster):
    href = 'https://meteoinfo.ru/rss/forecasts/index.php?s={town_id}'
    REGEX = re.compile(r"([а-яА-Я -]+). Температура ночью (\d+)., днём (\d+).\. Ветер ([а-яА-Я-]+), (\d+) м/с\..+\b")

    def __init__(self):
        super().__init__()
        self.result = []

    def parse_result(self, result):

        bs = BeautifulSoup(result, 'lxml')
        items = bs.select('item')
        date = datetime.datetime.now()
        for item in items:
            title = item.select_one('title').text
            description = item.select_one('description').text
            matches = self.REGEX.findall(description)
            self.result.append(ForecastBase(date=date,
                                            temp_day=int(matches[0][2]),
                                            temp_night=int(matches[0][1]),
                                            condition=matches[0][0],
                                            wind_direction=matches[0][3],
                                            wind_speed=int(matches[0][4])))
            date+=datetime.timedelta(days=1)



class Yandex(Forecaster):
    href = 'https://yandex.ru/pogoda/{town_id}'

    def parse_result(self, result):
        bs = BeautifulSoup(result, 'html.parser')

        forecast_div_list = bs.select('div.forecast-briefly__day.swiper-slide')
        for forecast_div in forecast_div_list:
            date = datetime.datetime.strptime(forecast_div.select_one('time')['datetime'], '%Y-%m-%d %H:%M%z')
            temps = forecast_div.select('span.temp__value')
            self.result.append(ForecastBase(date=date,
                                            temp_day=int(temps[0].text),
                                            temp_night=int(temps[1].text),
                                            condition=forecast_div.select_one('div.forecast-briefly__condition').text,
                                            wind_direction='-',
                                            wind_speed=0))

    def __init__(self):
        super().__init__()
        self.result = []
