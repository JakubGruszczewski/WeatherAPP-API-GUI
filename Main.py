import requests
from Entry import chose_place
import Widget

api_key = #place your API key from openweather.org/api here
units = "metric"
city = chose_place()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    Widget.widget(data)
elif response.status_code == 404:
    print("Searched place has not been found")
    exit()
else:
    print("Error had occured")
    exit()