import speech_recognition as sr
import pyttsx3
import time
# pip install pyttsx3
# pip install wikipedia
# pip install SpeechRecognition
#pip install PyAudio

# --- Setup pyttsx3 voice engine ---
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # You can change 1 to 0 for a male voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

# --- Simple Chatbot Logic ---
class SimpleChatbot:
    def __init__(self):
        self.chat_history = []

    def get_response(self, user_input: str) -> str:
        responses = {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! What's on your mind?",
            "how are you": "I'm doing great, thanks for asking! How about you?",
            "what is your name": "I'm GrokBot, nice to meet you!",
            "bye": "Goodbye! Come back anytime.",
            "help me": "I can answer simple questions or chat with you. Try saying 'hi', 'how are you', or 'bye' to exit.",
            "what can you do": "I can answer simple questions and chat with you! Try saying hi or ask for help.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything! Haha!",
            "tell me a fact": "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!",
            "what is the weather": "I can't check the weather right now, but you can try asking a weather app or website for the latest updates.",
            "what is your purpose": "I am here to assist you with simple questions and provide a friendly chat experience. How can I help you today?",
            "what is cuti": "Cuti is a voice assistant designed to help you with simple tasks and provide information through voice interaction. It's like having a friendly helper at your service!",
            "tell me about yourself": "I am cuti, your friendly voice assistant. I can help you with simple questions, provide information, and engage in friendly conversation.",
            "how are you": "I'm just a program, but I'm here to help you! How can I assist you today?",
        }

        user_input = user_input.lower().strip()
        for key in responses:
            if key in user_input:
                return responses[key]

        return "Sorry, I don't understand that. Try saying 'help' for options."

    def reset_chat(self):
        self.chat_history = []
        print("Chat history has been reset.")

# --- Voice Input Function ---
def listen_for_speech() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")
            return ""

# --- Main Chat Loop ---
def main():
    print("Welcome to cuti Voice Chat!")
    speak("Hello! I am cuti. How can I help you today?")
    chatbot = SimpleChatbot()

    while True:
        user_message = ""
        while not user_message:
            user_message = listen_for_speech()
            if not user_message:
                print("Try speaking again...")
                time.sleep(1)

        if user_message.lower() == 'exit':
            speak("Goodbye!")
            print("Chatbot: Goodbye!")
            break
        elif user_message.lower() == 'reset':
            chatbot.reset_chat()
            speak("Chat history reset.")
            continue

        response = chatbot.get_response(user_message)
        print(f"Chatbot: {response}")
        speak(response)

if __name__ == "__main__":
    main()
