# wxforecast

NWS weather forecast -> Pushover

## Requirements

* Python 3.6+
* Package requirements defined in `requirements.txt`
* A Pushover account and application (https://pushover.net/apps/build)

## Configuration

Configuration is via environment variables:

* `WXFORECAST_PUSHOVER_APP_KEY` - Pushover application key (https://pushover.net/apps/build)
* `WXFORECAST_COORDINATES` - latitude,longitude (eg. `39.0693,-94.6716`)
* `PUSHOVER_DEVICE` - Pushover device name
* `PUSHOVER_USER_KEY` - Pushover user key

## Setup Environment variables

`sudo -H gedit /etc/environment`


WXFORECAST_PUSHOVER_APP_KEY=YOURAPPKEY

WXFORECAST_COORDINATES=39.0693,-94.6716

PUSHOVER_DEVICE=weather

PUSHOVER_USER_KEY=YOURUSERKEY


Logout and relogin for the environment variables to loaded into the terminal session.
