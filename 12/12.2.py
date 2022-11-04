import requests
city_name = input('Give the city: ')
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},&limit={1}&appid=c9dca395b68f0f13b3cb7f4eedc59865"
response = requests.get(url)
data = response.json()
lat = data[0]['lat']
lon = data[0]['lon']
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid=c9dca395b68f0f13b3cb7f4eedc59865"
response = requests.get(url)
data = response.json()
print(data[0]['description'])