import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
client = Client(account_sid, auth_token)

api_key = "8e90bfb88ecdcd0607b4a6dc5e456b6c"
Lat = -6.9
Lng = 106.9
url= "https://api.openweathermap.org/data/2.5/forecast?"
data_count = 8
parameters = {"lat": Lat , "lon": Lng, "cnt":data_count, "appid": api_key}
send_data = ""
# data = {'cod': '200', 'message': 0, 'cnt': 8, 'list': [{'dt': 1772809200, 'main': {'temp': 296.75, 'feels_like': 297.62, 'temp_min': 296.75, 'temp_max': 296.75, 'pressure': 1013, 'sea_level': 1013, 'grnd_level': 917, 'humidity': 94, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 99}, 'wind': {'speed': 1.19, 'deg': 235, 'gust': 3.36}, 'visibility': 10000, 'pop': 0.51, 'sys': {'pod': 'n'}, 'dt_txt': '2026-03-06 15:00:00'}, {'dt': 1772820000, 'main': {'temp': 296.89, 'feels_like': 297.83, 'temp_min': 296.89, 'temp_max': 297.16, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 915, 'humidity': 96, 'temp_kf': -0.27}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 99}, 'wind': {'speed': 0.51, 'deg': 244, 'gust': 1.7}, 'visibility': 10000, 'pop': 0.33, 'sys': {'pod': 'n'}, 'dt_txt': '2026-03-06 18:00:00'}, {'dt': 1772830800, 'main': {'temp': 296.66, 'feels_like': 297.63, 'temp_min': 296.62, 'temp_max': 296.66, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 914, 'humidity': 98, 'temp_kf': 0.04}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'clouds': {'all': 98}, 'wind': {'speed': 0.8, 'deg': 255, 'gust': 1.52}, 'visibility': 10000, 'pop': 0.14, 'sys': {'pod': 'n'}, 'dt_txt': '2026-03-06 21:00:00'}, {'dt': 1772841600, 'main': {'temp': 298.18, 'feels_like': 299.22, 'temp_min': 298.18, 'temp_max': 298.18, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 916, 'humidity': 95, 'temp_kf': 0}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'clouds': {'all': 87}, 'wind': {'speed': 0.76, 'deg': 283, 'gust': 2.08}, 'visibility': 10000, 'pop': 0.05, 'sys': {'pod': 'd'}, 'dt_txt': '2026-03-07 00:00:00'}, {'dt': 1772852400, 'main': {'temp': 298.39, 'feels_like': 299.22, 'temp_min': 298.39, 'temp_max': 298.39, 'pressure': 1012, 'sea_level': 1012, 'grnd_level': 916, 'humidity': 86, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 100}, 'wind': {'speed': 1.97, 'deg': 256, 'gust': 4.17}, 'visibility': 10000, 'pop': 0.21, 'rain': {'3h': 0.12}, 'sys': {'pod': 'd'}, 'dt_txt': '2026-03-07 03:00:00'}, {'dt': 1772863200, 'main': {'temp': 298.52, 'feels_like': 299.18, 'temp_min': 298.52, 'temp_max': 298.52, 'pressure': 1009, 'sea_level': 1009, 'grnd_level': 914, 'humidity': 79, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': {'all': 97}, 'wind': {'speed': 3.16, 'deg': 258, 'gust': 4.29}, 'visibility': 9165, 'pop': 1, 'rain': {'3h': 1.74}, 'sys': {'pod': 'd'}, 'dt_txt': '2026-03-07 06:00:00'}, {'dt': 1772874000, 'main': {'temp': 296.89, 'feels_like': 297.54, 'temp_min': 296.89, 'temp_max': 296.89, 'pressure': 1008, 'sea_level': 1008, 'grnd_level': 913, 'humidity': 85, 'temp_kf': 0}, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'clouds': {'all': 91}, 'wind': {'speed': 3.05, 'deg': 263, 'gust': 4.83}, 'visibility': 6210, 'pop': 1, 'rain': {'3h': 3.11}, 'sys': {'pod': 'd'}, 'dt_txt': '2026-03-07 09:00:00'}, {'dt': 1772884800, 'main': {'temp': 293.79, 'feels_like': 294.49, 'temp_min': 293.79, 'temp_max': 293.79, 'pressure': 1011, 'sea_level': 1011, 'grnd_level': 915, 'humidity': 99, 'temp_kf': 0}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'clouds': {'all': 87}, 'wind': {'speed': 1.49, 'deg': 232, 'gust': 3.1}, 'visibility': 10000, 'pop': 1, 'rain': {'3h': 1.76}, 'sys': {'pod': 'n'}, 'dt_txt': '2026-03-07 12:00:00'}], 'city': {'id': 1626381, 'name': 'Sukabumi', 'coord': {'lat': -6.9, 'lon': 106.9}, 'country': 'ID', 'population': 276414, 'timezone': 25200, 'sunrise': 1772751465, 'sunset': 1772795407}}

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
    # data_code = data['list'][n]["weather"][0]['id']
    # data_main = data['list'][n]["weather"][0]['main']
    data_desc = select_data["weather"][0]['description']
    data_humid = select_data["main"]['humidity']
    data_temp = round(select_data["main"]['temp']-273.1, 1)
    # send_data += data
    send_data += f"{data_time} / {data_temp}°C / {data_humid}% / {data_desc} \n"

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body= send_data,
  to='whatsapp:+62811712175'
)

print(message.sid)
