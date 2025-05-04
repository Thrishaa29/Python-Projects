# Jarvis - Voice Assistant in Python

Jarvis is a simple voice-activated personal assistant built with Python. It can perform a variety of tasks such as searching Wikipedia, opening websites, playing music, telling the time, and sending emails via voice commands.

## Features

- **Voice Recognition**: Uses the `speech_recognition` library to take commands via microphone input.
- **Text-to-Speech**: Replies with spoken responses using the `pyttsx3` library.
- **Wikipedia Search**: Searches and reads summaries from Wikipedia.
- **Web Navigation**: Opens popular websites like YouTube, Google, and Spotify.
- **Time Reporting**: Tells the current time.
- **Email Sending**: Sends emails using Gmail SMTP.
- **Custom Greetings**: Greets the user based on the time of day.

## Requirements

- Python 3.x
- Internet connection for web features and voice recognition

### Python Libraries Used

- `pyttsx3`
- `wikipedia`
- `speech_recognition`
- `datetime`
- `webbrowser`
- `smtplib`

Install dependencies using:

```bash
pip install pyttsx3 wikipedia SpeechRecognition

