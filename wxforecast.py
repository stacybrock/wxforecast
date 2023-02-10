import os
import sys

import backoff
import nwswx
import requests


EMAIL = os.getenv('WXFORECAST_EMAIL', None)
if EMAIL is None or EMAIL == '':
    print('Error: missing or empty WXFORECAST_EMAIL environment variable!')
    sys.exit(1)

(LAT, LON) = [c.strip() for c in os.getenv('WXFORECAST_COORDINATES',
                                           '39.0693,-94.6716').split(',')]

@backoff.on_exception(backoff.expo,
                      requests.exceptions.ConnectionError,
                      max_time=60) # seconds
def get_forecast():
    nws = nwswx.WxAPI(EMAIL)
    return nws.point_forecast(LAT, LON,return_format=nwswx.formats.JSONLD)

def main():
    result = get_forecast()
    forecast = result['periods'][0]

    # create pushover notification
    title = f"{forecast['shortForecast']}"
    msg = f"""{forecast['detailedForecast']}

    Temp: {forecast['temperature']}°{forecast['temperatureUnit']}
    Wind: {forecast['windSpeed']} {forecast['windDirection']}
    Details: https://forecast.weather.gov/MapClick.php?lon={LON}&lat={LAT}
    """
    r = requests.post('https://api.pushover.net/1/messages.json', data = {
        'token': os.environ['WXFORECAST_PUSHOVER_APP_KEY'],
        'user': os.environ['PUSHOVER_USER_KEY'],
        'message': msg,
        'title': title,
        'device': os.environ['PUSHOVER_DEVICE']
    })


if __name__ == '__main__':
    main()
