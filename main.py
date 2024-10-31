import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

END_POINT= "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWM_API_KEY")

account_sid = os.environ.get("OWM_ACCT_SID")
auth_token = os.environ.get("OWM_AUTH")

proxy_client = TwilioHttpClient()
proxy = None
if 'https_proxy' in os.environ:
       proxy = os.environ['https_proxy']

proxy_client.session.proxies = {'https':proxy}

parameters = {
    "lat": 37.386051,
    "lon": -122.083855,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

response = requests.get(END_POINT, params= parameters)
response.raise_for_status()
weather_data = response.json()['weather']
# weather_id = int(response.json()['weather'][:12])


for weather_id in weather_data:
    i = int(weather_id['id'])
    client = Client(account_sid, auth_token, http_client=proxy_client)
    if i < 700:
        message = client.messages.create(
            body="Bring the Umbrella",
            from_="+18888671995",
            to= "+16786752287"
        )
    else:
        message = client.messages.create(
            body="You don't need it",
            from_="+18888671995",
            to="+16786752287"
        )

    print(message.status)
    print(message.sid)