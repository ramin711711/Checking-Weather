import requests
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
        }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        sys = data['sys']
        coord = data['coord']

        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_description = weather['description']
        wind_speed = wind['speed']
        sunrise = sys['sunrise']
        sunset = sys['sunset']
        country = sys['country']

        from datetime import datetime
        sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
        sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')

        print(f"Weather in {city.capitalize()}, {country.capitalize()}:")
        print(f"Coordinates: Latitude {coord['lat']}, Longitude {coord['lon']}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather Description: {weather_description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Sunrise: {sunrise_time}")
        print(f"Sunset: {sunset_time}")
    else:
        print(f'Error, unable to get weather data. Status code: {response.status_code}')

if __name__ == "__main__":
    api_key = '84ece90801f8623a75592cd4a875b3e2'
    city = input("Enter the city name: ")
    get_weather(api_key, city)


# import requests

# def get_weather(api_key, city):
#     # Define the base URL and parameters for the API request
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {
#         'q': city,
#         'appid': api_key,
#         'units': 'metric'  # Use 'imperial' for Fahrenheit
#     }

#     # Make the API request
#     response = requests.get(base_url, params=params)

#     # Check if the request was successful
#     if response.status_code == 200:
#         data = response.json()
#         main = data['main']
#         weather = data['weather'][0]
        
#         # Extract and print relevant information
#         temperature = main['temp']
#         weather_description = weather['description']
#         print(f"Weather in {city}:")
#         print(f"Temperature: {temperature}°C")
#         print(f"Description: {weather_description.capitalize()}")
#     else:
#         print(f"Error: Unable to fetch weather data. Status code {response.status_code}")

# if __name__ == "__main__":
#     # Your OpenWeatherMap API key
#     api_key = '84ece90801f8623a75592cd4a875b3e2'
#     city = input("Enter the city name: ")
#     get_weather(api_key, city)
