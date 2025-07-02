# Cuti 3.0 - An Advanced Voice Assistant
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
engine.setProperty('rate', 150)  # Set speaking rate
# --- Setup logging ---
logging.basicConfig(level=logging.INFO)
# Create a log file with timestamp
if not os.path.exists('cuti_assistant.log'):
    with open('cuti_assistant.log', 'w') as f:
        pass  # Create the log file if it doesn't exist
# Configure logging to write to a file

logging.basicConfig(filename='cuti_assistant.log', level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration file
CONFIG = {
    "version": "3.0",
    "music_dir": os.path.expanduser("~/Music/"),
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

def find_application(app_name: str) -> [str]:
    """Dynamically locate application paths."""
    user = os.getlogin()
    for path in CONFIG["app_paths"].get(app_name, []):
        path = path.format(user)
        if os.path.exists(path):
            return path
    return None        

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


class Chatbot:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.mistral.ai/v1/chat/completions"
        self.chat_history: List[Dict[str, str]] = []
        self.max_history_length = 10  # Limit chat history to 10 user-assistant pairs
        self.model = "mistral-small-latest"  # Default model
        self.chat_history = []
        self.language = "en"

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

def listen_for_speech() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            # 🛑 THIS is where the crash happens, so we wrap it in try-except
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
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
        if 'open wikipedia' in query:
            if not check_internet():
                speak("No internet for Wikipedia search.")
                continue
            query = query.replace("wikipedia", "").strip()
            try:
                speak(f"Searching Wikipedia for {query}")
                print(f"Searching Wikipedia for {query}")
                import wikipedia  # moved import here to avoid crash if not used
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
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    song_path = os.path.join(music_dir, random.choice(songs))
                    os.startfile(song_path)
                    speak("Playing music from your local directory.")
                else:

                    speak("No songs found in your music directory.")
            else:
                speak("Music directory not found. Opening Spotify.")
                webbrowser.open("https://open.spotify.com")
            command_executed = True

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")
            command_executed = True

        elif 'open code' in query:
            code_path = find_application("code")
            if code_path:
                os.startfile(code_path)
                speak("Opening Visual Studio Code.")
            else:
                speak("Code editor not found.")
            command_executed = True

        elif 'email to biplav' in query:
            try:
                speak("What should I say?")
                content = listen_for_speech()
                to = CONFIG["default_email"]
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email.")    
if __name__ == "__main__":
        load_config()
        if check_internet():        
            print("Internet is available. Starting Cutie Assistant...")
            speak("Internet is available. Starting Cutie Assistant...")
            main()
           
        else:
            print("No internet connection. Please check your network settings.")
            speak("No internet connection. Please check your network settings.")    
# -*- coding: utf-8 -*- 
# Cuti 3.0 - An Advanced Voice Assistant
# This code is a more advanced version of the Cuti voice assistant, featuring improved error handling,
# dynamic application path resolution, and enhanced chatbot capabilities.
# The code includes features like speech recognition, text-to-speech, internet checks, and more.
# It also supports a chatbot interface using the Mistral AI API, allowing for natural language interactions.
# The code is designed to be modular and easily extensible, allowing for future enhancements and features.
# The assistant can perform tasks like opening applications, sending emails, playing music, and answering questions



 