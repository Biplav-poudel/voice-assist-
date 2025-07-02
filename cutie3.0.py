<<<<<<< HEAD
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random
import subprocess
import time
import json
import re
import getpass
import socket
import datetime
import logging
from typing import Optional, Dict
from urllib.request import urlopen


 #pip install PyAudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# Function to check microphone and speaker functionality
=======
import speech_recognition as sr
import pyttsx3
import time
import requests
import datetime
import json
import os
import sys
import smtplib
import random
import subprocess
import re
import getpass
import socket
import logging
import webbrowser
from typing import Dict, List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set console encoding to UTF-8 to handle Unicode characters (e.g., emojis)
sys.stdout.reconfigure(encoding='utf-8')

# --- Setup pyttsx3 voice engine ---
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # You can change 1 to 0 for a male voice

>>>>>>> 0a2acfb (last commit)

logging.basicConfig(filename='cuti_assistant.log', level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration file
CONFIG = {
<<<<<<< HEAD
    "music_dir": os.path.expanduser("~/Music/nepali_songs"),
=======
    "music_dir": os.path.expanduser("~/Music/"),
>>>>>>> 0a2acfb (last commit)
    "app_paths": {
        "code": [
            "C:\\Users\\{}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
            "/Applications/Visual Studio Code.app/Contents/MacOS/Electron"
        ],
        "notepad": ["C:\\Windows\\System32\\notepad.exe"]
    },
    "default_email": "youremail@gmail.com",
    "language": "en-in"
}

# Save/load config
CONFIG_FILE = "cuti_config.json"
def save_config():
    with open(CONFIG_FILE, 'w') as f:
        json.dump(CONFIG, f)

if not os.path.exists(CONFIG_FILE):
    save_config()

def load_config():
    global CONFIG
    try:
        with open(CONFIG_FILE, 'r') as f:
            CONFIG.update(json.load(f))
    except FileNotFoundError:
        pass

def check_internet() -> bool:
    """Check if internet is available."""
    try:
        socket.create_connection(("www.google.com", 80), timeout=2)
        return True
    except OSError:
        return False

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

<<<<<<< HEAD
def check_microphone():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Microphone test: Please say something...") 
            speak("Microphone test: Please say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=2, )

        print("Mic working. Recognizing...")
        speak("Microphone test successful. Please wait while I recognize your speech.")
        text = recognizer.recognize_google(audio)
        print("Your said:", text)
        speak("your said: " + text)
        return True

    except sr.WaitTimeoutError:
        print("Mic timeout. No voice detected.")
        speak("Microphone test failed. No voice detected.")
        speak("Please ensure your microphone is connected and try again.")
        return False
    except sr.UnknownValueError:
        print("Couldn't understand what you said.")
        speak(" I couldn't understand what you said.")
        return False
    except sr.RequestError as e:
        print(f"Could not connect to Google API: {e}")
        speak("could not connect to Google API.")
        speak("Please check your internet connection and try again.")
        return False
    except Exception as e:
        print(f"Microphone error: {e}")
        speak(f"Microphone error: {e}")
        return False

def check_speaker() -> bool:
    """Test speaker functionality."""
    try:
        speak("Testing speaker. If you hear this, your speaker is working.")
        print("Speaker test completed.")
        logging.info("Speaker test passed")
        return True
    except Exception as e:
        logging.error(f"Speaker error: {e}")
        speak(f"Speaker error: {e}")
        print(f"Speaker error: {e}")
        return False

def find_application(app_name: str) -> Optional[str]:
=======


def find_application(app_name: str) -> [str]:
>>>>>>> 0a2acfb (last commit)
    """Dynamically locate application paths."""
    user = os.getlogin()
    for path in CONFIG["app_paths"].get(app_name, []):
        path = path.format(user)
        if os.path.exists(path):
            return path
    return None        

<<<<<<< HEAD

=======
>>>>>>> 0a2acfb (last commit)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")
        print("Hello, I am Cutie. How may I help you?")
    speak("Hello, I am Cutie.")
    speak("I am a voice assistant. I can help you with simple tasks and answer questions.")

<<<<<<< HEAD
# --- Preload Joke Responses ---
joke_responses = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? Because it had too many problems!",
    "Why don’t programmers like nature? It has too many bugs.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why was the computer cold? It forgot to close its Windows.",
    "Why did the student eat his homework? Because the teacher told him it was a piece of cake!",
    "Why was six afraid of seven? Because 7 8 9!",
    "What did the janitor say when he jumped out of the closet? Supplies!"
]

# --- Preload Fact Responses ---
fact_responses = [
    "Octopuses have three hearts and can change color.",
    "Bananas are berries, but strawberries aren't!",
    "The shortest war in history lasted only 38 minutes.",
    "Honey never spoils—you can eat 3000-year-old honey!",
    "There are more stars in the universe than grains of sand on Earth.",
    "Sharks existed before trees were even a thing.",
    "Some cats are allergic to humans.",
    "Your body has more bacterial cells than human ones.",
    "The Eiffel Tower can grow taller in summer.",
    "A bolt of lightning is five times hotter than the sun's surface."
]

# --- Preload Compliment Responses ---
compliment_responses = [
    "You're doing amazing, don't stop!",
    "Your ideas are always so creative!",
    "You're like a coding wizard!",
    "You're a quick learner and it shows!",
    "You've got great energy today!",
    "You light up the room just by existing!",
    "You’re smarter than you think!",
    "I admire your dedication and hard work!",
    "You’re full of good ideas!",
    "You’re going to do great things!"
]
# --- Simple Chatbot Class ---
# This class handles the chatbot's responses and chat history.

class SimpleChatbot:
    def __init__(self):
        self.chat_history = []
        self.language = "en"
=======

class Chatbot:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.mistral.ai/v1/chat/completions"
        self.chat_history: List[Dict[str, str]] = []
        self.max_history_length = 10  # Limit chat history to 10 user-assistant pairs
        self.model = "mistral-small-latest"  # Default model
        self.chat_history = []
        self.language = "en"

>>>>>>> 0a2acfb (last commit)
    def add_to_history(self, user_input: str, response: str):
        """Add user input and response to chat history."""
        self.chat_history.append({"user": user_input, "bot": response})
        if len(self.chat_history) > 10:
            self.chat_history.pop(0)
    def get_chat_history(self) -> str:
        """Get the chat history as a formatted string."""
        history = "\n".join([f"You: {entry['user']}\nCuti: {entry['bot']}" for entry in self.chat_history])
        return history if history else "No chat history available."

    def set_language(self, match):
        """Set the language for the chatbot."""
        lang = match.group(1).lower()
        if lang == "english":
            self.language = "en"
            return "Language set to English."
        elif lang == "nepali":
            self.language = "ne"
            return "भाषा नेपालीमा सेट गरियो।"
        else:
<<<<<<< HEAD
            return f"Sorry, I don't support the language '{lang}' yet."

    def get_response(self, user_input: str) -> str:
        # --- Preload Joke Responses ---
        responses = {
            r"^tell me a joke$": lambda match: random.choice(joke_responses),
            r"^tell me a fact$": lambda match: random.choice(fact_responses),
            r"^give me a compliment$": lambda match: random.choice(compliment_responses),
            r"^(hi|hello|hey)$": lambda match: "Hi there! What's up?",
            r"^(how are you|how's it going|how r u)$": lambda match: "I'm doing awesome, thanks! How about you?",
            r"^(what is your name|who are you)$": lambda match: "I'm Cuti, your smart little assistant!",
            r"^(bye|exit|quit)$": lambda match: "Catch you later! Goodbye!",
            r"^what time is it$": lambda match: f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
            r"^what day is it$": lambda match: f"Today is {datetime.datetime.now().strftime('%A')}",

            r"^(help|what can you do)$": "I can chat, open apps, search Wikipedia, play music, set reminders, do math, and more! Try saying 'tell me a joke' or 'open YouTube'.",
            r"^what is the weather$": "I need a city name to check the weather. Say something like 'weather in New York'.",
            r"^what is your purpose$": "I'm here to make your life easier with voice commands and fun chats!",
            r"^tell me about yourself$": "I'm Cuti, built to assist with tasks, answer questions, and sprinkle some humor!",
            r"^(fuck you|fuck u)$": "Whoa, let's keep it friendly! How can I help you now?",
            r"^(i love you|love you)$": "Aww, that's sweet! I'm just a bot, but I appreciate the love!",
            r"^who made you$": "I was created by Biplav to assist folks like you!",
            r"^what time is it$": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
            r"^what day is it$": f"Today is {datetime.datetime.now().strftime('%A')}.",
            r"^how old are you$": "I'm timeless, but I was born in 2025, so I'm fresh and ready to help!",
            r"^tell me a story$": "Once upon a time, a curious user asked Cuti for a story, and I spun a tale of adventure... Want a longer one?",
            r"^what is love$": "Baby, don't hurt me, don't hurt me, no more! 😄 Love's a big topic—want a philosophical or funny take?",
            r"^are you human$": "Nope, I'm a digital buddy, but I can chat like the best of 'em!",
            r"^what is the meaning of life$": "42, according to Douglas Adams! Or maybe it's about finding joy—your pick!",
            r"^set language to (\w+)$": self.set_language

        }

        for pattern, response in responses.items():
            match = re.match(pattern, user_input)
            if match:
                if callable(response):
                    return response(match)
                return response

        # Handle math calculations
        if re.match(r"^(calculate|what is)\s+(.+)$", user_input):
            calc_input = re.match(r"^(calculate|what is)\s+(.+)$", user_input).group(2)
            try:
                result = eval(calc_input, {"__builtins__": {}})
                return f"The result is {result}."
            except Exception:
                return "Sorry, I couldn't calculate that. Try a simple math expression like '2 + 2'."

        return "I didn't catch that. Try saying 'help' for ideas!"
        

    def reset_chat(self):
        self.chat_history = []
        speak("Chat history has been reset.")
        print("Chat history has been reset.")
=======
            return f"Sorry, I don't support the language '{lang}' yet."    


    def get_response(self, user_input: str) -> str:
        """Get a response from the Mistral AI API for the given user input."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        messages = self.chat_history + [{"role": "user", "content": user_input}]
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 100,
            "temperature": 0.7,
            "top_p": 1.0,
            "stream": False
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
            result = response.json()
            bot_response = result.get("choices", [{}])[0].get("message", {}).get("content", "Sorry, I couldn't process that.")
            self.chat_history.append({"role": "user", "content": user_input})
            self.chat_history.append({"role": "assistant", "content": bot_response})
            if len(self.chat_history) > self.max_history_length * 2:
                self.chat_history = self.chat_history[-self.max_history_length * 2:]
            return bot_response
        except requests.RequestException as e:
            print(f"API request failed: {e}")
            return f"Error connecting to the API: {str(e)}"

    def reset_chat(self) -> None:
        """Reset the chat history."""
        self.chat_history = []
        print("Chat history has been reset.")
        speak("Chat history has been reset.")
        

>>>>>>> 0a2acfb (last commit)

def listen_for_speech() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
<<<<<<< HEAD
       
        print("Listening...")

        r.pause_threshold = 4  # Adjust pause threshold for better recognition

        try:
            # 🛑 THIS is where the crash happens, so we wrap it in try-except
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
=======
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            # 🛑 THIS is where the crash happens, so we wrap it in try-except
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
>>>>>>> 0a2acfb (last commit)
            return r.recognize_google(audio, language=CONFIG["language"])
        except sr.UnknownValueError:    
            print("Could not understand the audio.")
            speak("I didn't catch that. Could you please repeat?")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            speak("Listening timed out. No speech detected.")
            return ""
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("I can't connect to the speech service. Please check your internet.")
        return ""
    except Exception as e:
        print(f"Unexpected recognition error: {e}")
        speak("say something.")
        return ""

<<<<<<< HEAD
        
    
def main():
    wishMe()
    chatbot = SimpleChatbot()

    while True:
        user_message = ""
        while not user_message:
            user_message = listen_for_speech()
            if not user_message:
                speak("I didn't hear anything. Please try again.")
                time.sleep(1)

        if user_message.lower().strip() in ['exit', 'quit', 'bye']:
            speak("Goodbye!")
            break
        elif user_message.lower().strip() == 'reset':
            chatbot.reset_chat()
            continue

        response = chatbot.get_response(user_message)
        print(f"Cuti: {response}")
        speak(response)

        query = user_message.lower()
=======

def main():
    wishMe()
    
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        speak("API key not found. Please set the MISTRAL API key.")
        return

    chatbot = Chatbot(api_key)

    while True:
        user_message = listen_for_speech()
        if not user_message:
            continue

        query = user_message.lower()

        if query in ['exit', 'quit', 'bye']:
            speak("Goodbye!")
            break

        elif query == 'reset':
            chatbot.reset_chat()
            continue

        elif query == 'what is your name':
            speak("I am Cutie, your voice assistant.")
            continue    

        command_executed = False

        # === Task Commands ===
>>>>>>> 0a2acfb (last commit)
        if 'open wikipedia' in query:
            if not check_internet():
                speak("No internet for Wikipedia search.")
                continue
            query = query.replace("wikipedia", "").strip()
            try:
<<<<<<< HEAD
=======
                import wikipedia  # moved import here to avoid crash if not used
>>>>>>> 0a2acfb (last commit)
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                logging.info(f"Wikipedia search: {query}")
            except wikipedia.DisambiguationError:
                speak("Please be more specific with your search.")
            except wikipedia.PageError:
                speak("No matching Wikipedia page found.")
            except Exception as e:
                speak("Error fetching Wikipedia data.")
                logging.error(f"Wikipedia error: {e}")
<<<<<<< HEAD

        elif 'open youtube' in query:
            speak("Opening YouTube")
            print("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            print("Opening Google")
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            speak("Opening Spotify")
            print("Opening Spotify")
            webbrowser.open("https://open.spotify.com")

        elif 'play music' in query:
            speak("Playing music")
            print("Playing music")
            music_dir = 'D:\\Non Critical\\songs\\nepali songs'
=======
            command_executed = True

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
            command_executed = True

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")
            command_executed = True

        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com")
            command_executed = True

        elif 'play music' in query:
            music_dir = CONFIG["music_dir"]
>>>>>>> 0a2acfb (last commit)
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    song_path = os.path.join(music_dir, random.choice(songs))
                    os.startfile(song_path)
                    speak("Playing music from your local directory.")
                else:
<<<<<<< HEAD
                    speak("No songs found in the music directory.")
            else:
                speak("Music directory not found. Opening Spotify web player instead.")
                webbrowser.open("https://open.spotify.com")
=======
                    speak("No songs found in your music directory.")
            else:
                speak("Music directory not found. Opening Spotify.")
                webbrowser.open("https://open.spotify.com")
            command_executed = True
>>>>>>> 0a2acfb (last commit)

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
<<<<<<< HEAD

        elif 'open code' in query:
            speak("Opening Visual Studio Code")
            print("Opening Visual Studio Code")
            codePath = "C:\\Users\\Biplav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
=======
            command_executed = True

        elif 'open code' in query:
            code_path = find_application("code")
            if code_path:
                os.startfile(code_path)
                speak("Opening Visual Studio Code.")
            else:
                speak("Code editor not found.")
            command_executed = True
>>>>>>> 0a2acfb (last commit)

        elif 'email to biplav' in query:
            try:
                speak("What should I say?")
                content = listen_for_speech()
<<<<<<< HEAD
                to = "youremail@gmail.com"  # Replace with actual email
=======
                to = CONFIG["default_email"]
>>>>>>> 0a2acfb (last commit)
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email.")
<<<<<<< HEAD
        elif 'open notepad' in query:
            speak("Opening Notepad")
            print("Opening Notepad")
            notepadPath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepadPath)           

if __name__ == "__main__":
    mic_ok = check_microphone()
    speaker_ok = check_speaker()
    if mic_ok and speaker_ok:
        speak("All systems ready! Let's get started.")
        logging.info("System check passed")
=======
            command_executed = True

        elif 'open notepad' in query:
            notepad_path = find_application("notepad")
            if notepad_path:
                os.startfile(notepad_path)
                speak("Opening Notepad.")
            else:
                speak("Notepad not found.")
            command_executed = True

        # === Chatbot Fallback ===
        if not command_executed:
            response = chatbot.get_response(user_message)
            chatbot.add_to_history(user_message, response)
            print(f"You: {user_message}")
            print(f"Cuti: {response}")
            speak(response)

    
if __name__ == "__main__":
>>>>>>> 0a2acfb (last commit)
        load_config()
        if check_internet():        
            print("Internet is available. Starting Cutie Assistant...")
            speak("Internet is available. Starting Cutie Assistant...")
            main()
           
        
<<<<<<< HEAD
    else:
        speak("Hardware check failed. Please fix microphone or speaker issues.")
        logging.error("System check failed")

# Cuti 2.0 - An Advanced Voice Assistant
=======
    
# Cuti 3.0 - An Advanced Voice Assistant
>>>>>>> 0a2acfb (last commit)
# This code is a more advanced version of the Cuti voice assistant, featuring improved error handling,
# dynamic application path resolution, and enhanced chatbot capabilities.


<<<<<<< HEAD
=======




>>>>>>> 0a2acfb (last commit)
