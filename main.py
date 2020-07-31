
import Forecast.meteoinfo as meteo
import re
if __name__=="__main__":
    m = meteo.Meteoinfo()
    m.get_forecast(town_id=26063, date=None)
    print(m.get_result())

    y = meteo.Yandex()
    y.get_forecast(town_id='saint-petersburg', date=None)
    print(y.get_result())

