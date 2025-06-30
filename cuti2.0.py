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


 #pip install PyAudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# Function to check microphone and speaker functionality


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def check_microphone():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Microphone test: Please say something...") 
            speak("Microphone test: Please say something...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

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

def check_speaker():
    try:
        engine = pyttsx3.init('sapi5')
        speak("Testing speaker...")
        print("Testing speaker...")
        engine.say("Speaker test successful. If you heard this, your speaker is working.")
        engine.runAndWait()
        speak("Speaker test completed.")
        print("Speaker test completed.")
        return True
    except Exception as e:
        speak(f"Speaker error: {e}")
        print(f"Speaker error: {e}")
        return False

# Run both tests
if __name__ == "__main__":
    mic_ok = check_microphone()
    speaker_ok = check_speaker()

    if mic_ok and speaker_ok:
        speak("All systems go! Microphone and speaker are working.")
        print("\nAll systems go! Microphone and speaker are working.")
    else:
        speak("One or more devices are not working. Please check them.")
        print("\nOne or more devices are not working. Please check them.")



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
    speak("Hello, I am Cutie. How may I help you?")

def chatbot_response(user_input):
    # Dictionary of responses for specific inputs
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What's on your mind?",
        "how are you": "I'm doing great, thanks for asking! How about you?",
        "what is your name": "I'm GrokBot, nice to meet you!",
        "bye": "Goodbye! Come back anytime.",
        "help": "I can answer simple questions or chat with you. Try saying 'hi', 'how are you', or 'bye' to exit."
    }
    
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    # Check if input matches any key in responses
    for key in responses:
        if key in user_input:
            return responses[key]
    
    # Default response for unknown inputs
    speak("Sorry, I don't understand that. Try saying 'help' for options.")
    return "Sorry, I don't understand that. Try saying 'help' for options."



def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open spotify' in query:  # Combined 'open spotify' and 'play music'
            spotify_path = r"C:\Users\Biplav\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\spotify.lnk"
            spotify_uris = [
                "spotify:track:7qiZfU4dY1lWllzX7mPBI3",  # Shape of You
                "spotify:track:4uLU6hMCjMI75M1A2tKUQC",  # Rick Astley - Never Gonna Give You Up
                "spotify:track:3n3Ppam7vgaVa1iaRUc9Lp",  # Eminem - Lose Yourself
                "spotify:track:2b8fOow8UzyDFAE27YhOZM",  # Harry Styles - As It Was
                "spotify:track:1rgnBhdG2JDFTbYkYRZAku"   # Imagine Dragons - Believer
            ]
            spotify_web_links = [
                "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3",
                "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC",
                "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp",
                "https://open.spotify.com/track/2b8fOow8UzyDFAE27YhOZM",
                "https://open.spotify.com/track/1rgnBhdG2JDFTbYkYRZAku"
            ]

            if os.path.exists(spotify_path):
                 speak("Spotify app found. Opening Spotify app...")
                 os.startfile(spotify_path)  # Open Spotify app 
                 # Wait for Spotify to launch
                 song_uri = random.choice(spotify_uris)
                 os.system(f"start {song_uri}")  # Play random song in app


        elif 'play music' in query:  # Alternative local music directory logic
            music_dir = 'D:\\Non Critical\\songs\\nepali songs'
            if not os.path.exists(music_dir):
                 speak("Music directory not found.")
                 print("Music directory not found.")
                # Fallback to Spotify web if local directory is not found
                 speak("Opening Spotify web player instead.")
                 webbrowser.open("open.spotify.com")
       

        elif ' what the  time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to biplav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "youremail@gmail.com"  # <- put the actual email here
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Bf. I am not able to send this email")
