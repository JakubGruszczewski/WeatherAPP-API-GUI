import requests
from Entry import chose_place
import Widget

api_key = #place your API key here
entry_block = chose_place()
unit = entry_block[1]
url = f"https://api.openweathermap.org/data/2.5/weather?q={entry_block[0]}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    Widget.widget(data, unit)
elif response.status_code == 404:
    print("Searched place has not been found")
    exit()
else:
    print("Error had occurred")
    exit()
