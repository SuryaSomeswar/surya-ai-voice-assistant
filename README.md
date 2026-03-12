# 🤖 Surya AI Voice Assistant

Surya is a simple **Python-based voice assistant** that listens to your voice commands and performs useful tasks such as playing music, telling the time, searching the web, opening websites, telling jokes, and more.

This project demonstrates the use of **speech recognition, text-to-speech, and automation using Python**.

---

## ✨ Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech responses
* 🎵 Play songs on YouTube
* ⏰ Tell current time
* 📅 Tell today's date
* 🌐 Open websites (Google, YouTube, LinkedIn, WhatsApp, Instagram)
* 🔍 Search anything on Google
* 📚 Fetch short information from Wikipedia
* 😂 Tell random programming jokes
* 💻 Open Visual Studio Code
* 🚪 Exit assistant using voice command

---

## 🛠️ Technologies Used

* **Python**
* `speech_recognition`
* `pyttsx3`
* `pywhatkit`
* `wikipedia`
* `pyjokes`
* `webbrowser`
* `datetime`

---

## 📦 Installation

1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/surya-ai-assistant.git
```

2️⃣ Navigate to the project folder

```bash
cd surya-ai-assistant
```

3️⃣ Install required libraries

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes pyaudio
```

⚠️ If `pyaudio` fails to install, install it using:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ Run the Assistant

```bash
python surya.py
```

After running the script, the assistant will start listening for commands.

---

## 🎙️ Example Voice Commands

You can try commands like:

* **"Play Believer song"**
* **"What is the time"**
* **"What is today's date"**
* **"Who is Elon Musk"**
* **"Tell me a joke"**
* **"Open YouTube"**
* **"Open Google"**
* **"Search artificial intelligence"**
* **"Exit"**

---

## 📁 Project Structure

```
surya-ai-assistant
│
├── surya.py
└── README.md
```

---

## 🚀 Future Improvements

Possible enhancements for the project:

* Add **weather information**
* Add **news update**

