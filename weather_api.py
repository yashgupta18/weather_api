import requests
from convert_kelvin_to_celsius import kelvin

api_call='http://api.openweathermap.org/data/2.5/weather?APPID=21c294cec6b1aea7b3493e98f7dd51fa&q='
place=input('Enter city:')
#key=21c294cec6b1aea7b3493e98f7dd51fa

#concatenate the input with api_call
url_weather=api_call+place


json_data=requests.get(url_weather).json()
data_temperature=json_data['main']['temp']
t=kelvin(data_temperature)

data_humidity=json_data['main']['humidity']
data_visibility=json_data['visibility']

print('temperature={}C,{}K \nhumdity={} \nvisibility={}'.format(t,data_temperature,data_humidity,data_visibility))