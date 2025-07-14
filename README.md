# Voice Assist

A Python-based voice-controlled assistant that recognizes your speech, processes commands, and responds using speech synthesis.

## Features

- Speech recognition for voice commands
- Speech synthesis for responses
- Configurable via JSON and environment variables
- Logging of interactions and errors

## Project Structure

```
.
├── .env                 # Environment variables (API keys, secrets)
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── chatbot.py           # Main chatbot script
├── cuti_assistant.log   # Log file for chatbot activity
├── cuti_config.json     # Chatbot configuration
└── cutie3.0.py          # Additional chatbot module/version
```

## Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/Biplav-poudel/voice-assist-
cd voice-assist-
```

2. **Install dependencies**

Make sure you have Python 3.8+ installed, then install required packages:

```bash
pip install -r requirements.txt
```

3. **change  your `.env` file**

Create a `.env` file in the project root with your API keys and secrets. For example:

```env
API_KEY=your_api_key_here
OTHER_SECRET=your_other_secret_here
```

4. **Configure the chatbot**

Edit `cuti_config.json` to customize chatbot settings such as language, wake word, etc.

5. **Run the assistant**

Start the voice assistant by running:

```bash
python chatbot.py
```

Speak to the assistant through your microphone and it will respond accordingly.

## Logging

All interactions and errors are logged in the `cuti_assistant.log` file for troubleshooting and monitoring purposes.

## Contributing

Feel free to open issues or submit pull requests to improve the project!

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

---
*Created by Biplav Poudel*

## 🧑‍💻 Author

**Biplav Poudel**  
GitHub: [@Biplav-poudel](https://github.com/Biplav-poudel)

---

## 📈 Future Enhancements

- Add support for more languages and dialects

- Integrate with popular calendar and reminder apps

- Implement natural language understanding for better command accuracy

- Add voice personalization options (e.g., different assistant voices)

- Create a web or mobile interface for easier interaction

- Improve offline support and reduce dependency on internet access

- Expand command set with smart home device controls

- Add user authentication and profiles for personalized experience 

---

Thank you for exploring! Feel free to contribute or raise issues for improvements.
