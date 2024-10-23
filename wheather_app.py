import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("City not found. Please check your input.")

def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name:")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()
