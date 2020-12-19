from climacell_api.client import ClimacellApiClient
from config import climacellApiKey
import datetime

client = ClimacellApiClient(climacellApiKey)

def parseWeatherRealtime(location):
    r = client.realtime(lat=location["lat"], lon=location["lon"], fields=['temp', 'wind_gust'])
    return r.json()

def parseWeatherForecast(location):
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=5)
    r = client.forecast_daily(lat=location["lat"], lon=location["lon"], end_time=tomorrow.strftime('%Y-%m-%dT%H:%M:%S.%f%z'), start_time='now', fields=['temp'])
    return r.json()