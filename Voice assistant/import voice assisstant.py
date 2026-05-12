import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import requests

# --- 1. Initialization & Configuration ---
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 for male, 1 for female (varies by system)
engine.setProperty('rate', 175) # Speed of speech

WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY" # Replace with your actual API key

def speak(text):
    """Converts text to speech and prints it to the console."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Captures microphone input and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n[Listening...]")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio).lower()
            print(f"You: {command}")
            return command
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            speak("I didn't quite catch that. Could you repeat?")
        except sr.RequestError:
            speak("My speech service is down. Please check your internet connection.")
    return ""

# --- 2. Advanced Features (APIs and Integrations) ---

def get_weather(city):
    """Fetches weather data using OpenWeatherMap API."""
    if WEATHER_API_KEY == "YOUR_OPENWEATHER_API_KEY":
        speak("I cannot fetch the weather because the API key is missing.")
        return

    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(base_url)
        data = response.json()
        if data["cod"] != "404":
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            speak(f"The temperature in {city} is {temp} degrees Celsius with {desc}.")
        else:
            speak("I couldn't find that city.")
    except Exception as e:
        speak("I had trouble connecting to the weather service.")

def answer_question(query):
    """Uses Wikipedia to answer general knowledge questions."""
    speak("Let me look that up for you...")
    try:
        # Search wikipedia and return a 2-sentence summary
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(results)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are too many results for that topic. Could you be more specific?")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find any information on that topic.")
    except Exception:
        speak("I encountered an error while searching for the answer.")

# --- 3. Main Logic & Task Automation ---

def process_command(command):
    """Parses the user's command and triggers the appropriate function."""
    if not command:
        return True

    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It is currently {current_time}")

    elif 'date' in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {current_date}")

    elif 'weather in' in command:
        # Extract the city name from the command (e.g., "weather in london")
        city = command.split('weather in')[-1].strip()
        get_weather(city)

    elif 'who is' in command or 'what is' in command or 'tell me about' in command:
        # Remove trigger words to get the actual search query
        query = command.replace('who is', '').replace('what is', '').replace('tell me about', '').strip()
        answer_question(query)

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'search' in command:
        query = command.replace('search', '').strip()
        if query:
            speak(f"Searching the web for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What would you like me to search for?")

    elif 'stop' in command or 'exit' in command or 'goodbye' in command:
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("I am not sure how to help with that yet.")

    return True

def main():
    """Starts the voice assistant."""
    speak("Advanced systems initialized. How can I assist you today?")
    is_running = True
    while is_running:
        command = listen()
        is_running = process_command(command)

if __name__ == "__main__":
    main()