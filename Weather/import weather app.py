import requests

def get_weather(city_name):
    """
    Fetches weather data for a given city using a free, keyless API.
    """
    # We use wttr.in, a free weather service that requires NO API KEY!
    # The '?format=j1' at the end tells it to give us the data in JSON format.
    url = f"https://wttr.in/{city_name}?format=j1"

    try:
        # Make the request to the free API
        response = requests.get(url)
        response.raise_for_status() 
        
        # Parse the JSON data
        weather_data = response.json()
        
        # Extract the required information (the structure is slightly different here)
        current = weather_data["current_condition"][0]
        temp = current["temp_C"]
        humidity = current["humidity"]
        description = current["weatherDesc"][0]["value"]
        
        # Display the data
        print("\n" + "="*30)
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Condition: {description}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print("="*30 + "\n")

    except requests.exceptions.HTTPError:
        print(f"\nError: Could not find weather for '{city_name}'. Please check the spelling.\n")
    except Exception as err:
        print(f"\nAn unexpected error occurred: {err}\n")

# --- MAIN PROGRAM LOOP ---
if __name__ == "__main__":
    print("Welcome to the Python Weather App (No API Key Required!)")
    
    while True:
        # Handle User Input
        user_input = input("Enter a city name (or type 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            print("Exiting application. Goodbye!")
            break
            
        if user_input:
            get_weather(user_input)
        else:
            print("Please enter a valid city name.")