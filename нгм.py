import requests
import json


response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=55.622687&lon=37.301575&APPID=43ff578a4cc2afbd965f58c087c5b0ae&units=metric')
content = response.content.decode('utf8')
print(str(content))
