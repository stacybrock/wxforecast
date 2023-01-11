# wxforecast

NWS weather forecast ➡️  Pushover

## Requirements

* Python 3.6+
* Package requirements defined in `requirements.txt`
* A Pushover account and application (https://pushover.net/apps/build)

## Configuration

Configuration is via environment variables:

|ENV VAR|Description|
|----|----|
|`WXFORECAST_EMAIL`|Email address for NWS Weather Forecast API User-Agent string|
|`WXFORECAST_COORDINATES`|Latitude,Longitude (eg. `39.0693,-94.6716`)|
|`WXFORECAST_PUSHOVER_APP_KEY`|Pushover application key (https://pushover.net/apps/build)|
|`PUSHOVER_DEVICE`|Pushover device name|
|`PUSHOVER_USER_KEY`|Pushover user key|

All environment variables are required.
