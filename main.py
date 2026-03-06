import requests
import os
from twilio.rest import Client

account_sid = 'ACcc35f137e61f3428310fcd6ad8aace68'
auth_token = 'd6c3fd5c9dee6d66f7b05ccf369b6940'
client = Client(account_sid, auth_token)

api_key = "8e90bfb88ecdcd0607b4a6dc5e456b6c"
Lat = -6.9
Lng = 106.9
url= "https://api.openweathermap.org/data/2.5/forecast?"
data_count = 8
parameters = {"lat": Lat , "lon": Lng, "cnt":data_count, "appid": api_key}
send_data = ""

try:
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as the_error:
    print("error !!! : ", the_error)

for n in range(data_count):
    select_data = data['list'][n]
    data_time = select_data["dt_txt"]
    data_desc = select_data["weather"][0]['description']
    data_humid = select_data["main"]['humidity']
    data_temp = round(select_data["main"]['temp']-273.1, 1)
    send_data += f"{data_time} / {data_temp}°C / {data_humid}% / {data_desc} \n"

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body= send_data,
  to='whatsapp:+62811712175'
)

print(message.sid)
