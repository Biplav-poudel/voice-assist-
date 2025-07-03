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
    
# --- Simple Chatbot Logic ---
class SimpleChatbot:
    def __init__(self):
        self.chat_history = []

    def get_response(self, user_input: str) -> str:

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
    print("Welcome to cutie Voice Chat!")
    speak("Hello! I am cutie. How can I help you today?")
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