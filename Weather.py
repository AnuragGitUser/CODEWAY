import json
import urllib.request

def get_weather_data(location):
    api_key = 'gIDSkreC5OhtECrTGkAM5NpMlpDYxpt6'  # Get your API key from Tomorrow.io
    url = f'https://api.tomorrow.io/v4/timelines?location={location}&fields=temperature,temperatureApparent,humidity,windSpeed,weatherCode&units=metric&timesteps=current&apikey={api_key}'
    response = urllib.request.urlopen(url)
    if response.getcode() == 200:
        data = json.loads(response.read())
        return data
    else:
        print("Failed to fetch data. Please try again later.")
        return None

def get_weather_description(weather_code):
    # Dictionary mapping weather codes to descriptions
    weather_descriptions = {
        1000: "Clear",
        1001: "Cloudy",
        1100: "Mostly Clear",
        1101: "Partly Cloudy",
        1102: "Mostly Cloudy",
        2000: "Fog",
        2100: "Light Fog",
        3000: "Light Wind",
        3001: "Wind",
        3002: "Strong Wind",
        4000: "Drizzle",
        4001: "Rain",
        4200: "Light Rain",
        4201: "Heavy Rain",
        5000: "Snow",
        5001: "Flurries",
        5100: "Light Snow",
        5101: "Heavy Snow",
        6000: "Freezing Drizzle",
        6001: "Freezing Rain",
        6200: "Light Freezing Rain",
        6201: "Heavy Freezing Rain",
        7000: "Ice Pellets",
        7101: "Heavy Ice Pellets",
        7102: "Light Ice Pellets",
        8000: "Thunderstorm"
    }
    return weather_descriptions.get(weather_code, "Unknown")

def display_weather(data):
    if data and 'data' in data and 'timelines' in data['data'] and data['data']['timelines']:
        timeline = data['data']['timelines'][0]
        if 'intervals' in timeline and timeline['intervals']:
            values = timeline['intervals'][0]['values']
            temperature = values.get('temperature')
            apparent_temperature = values.get('temperatureApparent')
            humidity = values.get('humidity')
            wind_speed = values.get('windSpeed')
            weather_code = values.get('weatherCode')

            print("==== Weather Forecast Application using Python ====")
            if temperature is not None:
                print(f"Temperature: {temperature}°C")
            if apparent_temperature is not None:
                print(f"Apparent Temperature: {apparent_temperature}°C")
            if humidity is not None:
                print(f"Humidity: {humidity}%")
            if wind_speed is not None:
                print(f"Wind Speed: {wind_speed} m/s")
            if weather_code is not None:
                print(f"Weather Code: {weather_code}")
                print(f"Weather Description: {get_weather_description(weather_code)}")
        else:
            print("No data available for the specified location.")
    else:
        print("No data available for the specified location.")

def main():
    location = input("Enter the name of a city or a zip code: ")
    weather_data = get_weather_data(location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
