import requests

def get_weather(city):
    try:
        # Geocoding API (get latitude & longitude)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url)
        geo_response.raise_for_status()

        geo_data = geo_response.json()

        # ✅ Proper city validation
        if "results" not in geo_data or not geo_data["results"]:
            print("❌ Error: City not found. Please enter a valid city name.")
            return

        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]

        # Weather API
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()

        weather_data = weather_response.json()

        if "current_weather" not in weather_data:
            print("❌ Weather data not available.")
            return

        current = weather_data["current_weather"]

        # Display formatted output
        print("\n🌤 Weather Information")
        print("---------------------------")
        print(f"City: {city.title()}")
        print(f"Temperature: {current['temperature']}°C")
        print(f"Wind Speed: {current['windspeed']} km/h")
        print("---------------------------\n")

    except requests.exceptions.RequestException as e:
        print("❌ Failed to connect to API:", e)

    except Exception as e:
        print("❌ Unexpected error:", e)


city_name = input("Enter city name: ")
get_weather(city_name)