import requests
from Entry import chose_place
from Widget import widget
from Error_Widget import display_error


api_key = #insert your API key here
entry_block = chose_place()
unit = entry_block[1]
url = f"https://api.openweathermap.org/data/2.5/weather?q={entry_block[0]}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    widget(data, unit)
elif response.status_code == 404:
    message = "Searched place has not been found."
    display_error(message)
else:
    message = "An error had occurred."
    display_error(message)
