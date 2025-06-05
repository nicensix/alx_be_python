# weather.py

import requests

# Replace 'your_api_key' with your actual API key from WeatherAPI
API_KEY = "a65b1f4e2b204e28bcb73520250406"
BASE_URL = "http://api.weatherapi.com/v1/current.json"
LOCATION = "Texas"  # You can change this to any city

# Construct the full API request URL
url = f"{BASE_URL}?key={API_KEY}&q={LOCATION}"

# Fetch weather data
response = requests.get(url)
data = response.json()

# Extract relevant weather information
if "current" in data:
    temperature = data["current"]["temp_c"]  # Temperature in Celsius
    condition = data["current"]["condition"]["text"]  # Weather description

    print(f"Weather in {LOCATION}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
else:
    print("Error fetching weather data. Check API key or location.")