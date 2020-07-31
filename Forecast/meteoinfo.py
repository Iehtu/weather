import datetime
from bs4 import BeautifulSoup

from Forecast.forecast_base import ForecastBase, Forecaster

class Meteoinfo(Forecaster):
    href = 'https://meteoinfo.ru/rss/forecasts/index.php?s={town_id}'

    def parse_result(self, result):
        print(result)


class Yandex(Forecaster):
    href = 'https://yandex.ru/pogoda/{town_id}'

    def parse_result(self, result):
        bs = BeautifulSoup(result, 'html.parser')

        forecast_div_list = bs.select('div.forecast-briefly__day.swiper-slide')
        for forecast_div in forecast_div_list:
            print(forecast_div.select_one('time')['datetime'])
            temps = forecast_div.select('span.temp__value')
            print(int(temps[0].text))
            print(int(temps[1].text))
            print(forecast_div.select_one('div.forecast-briefly__condition').text)

