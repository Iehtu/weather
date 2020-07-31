
import Forecast.meteoinfo as meteo

if __name__=="__main__":
    m = meteo.Meteoinfo()
    m.get_forecast(town_id=26063, date=None)

    y = meteo.Yandex()
    y.get_forecast(town_id='moscow', date=None)

