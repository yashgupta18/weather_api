import requests
from convert_kelvin_to_celsius import kelvin

api_call='http://api.openweathermap.org/data/2.5/weather?APPID= *insert your API KEY HERE* ='
place=input('Enter city:')


#concatenate the input with api_call
url_weather=api_call+place


json_data=requests.get(url_weather).json()
data_temperature=json_data['main']['temp']
t=kelvin(data_temperature)

data_humidity=json_data['main']['humidity']
data_visibility=json_data['visibility']

print('temperature={}C,{}K \nhumdity={} \nvisibility={}'.format(t,data_temperature,data_humidity,data_visibility))
