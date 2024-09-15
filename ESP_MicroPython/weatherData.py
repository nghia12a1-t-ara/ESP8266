def getData(city_name):
    try:
        import urequests as requests
    except:
        import requests
    try:
        import ujson as json
    except:
        import json
    
    city = city_name
    api_key = "c73571ed393a19dc1603de078d7d3c6e"
    map_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    
    weather_data = requests.get(map_url)
    place = weather_data.json().get('name')
    temperature = weather_data.json().get('main').get('temp') - 273
    
    print(place)
    print(temperature)
