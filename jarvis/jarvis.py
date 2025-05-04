import pyttsx3
import wikipedia
import speech_recognition as sr 
import datetime
import webbrowser
import smtplib


engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("Good evening")

    speak("I am trisha. please tell me how may I help you")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('thrishaa.j29@gmail.com','Anusha@123')
    server.sendmail('thrishaa.j29@gmail.com',to, content)
    server.close()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    with open("microphone-results.wav","wb") as f:
        f.write(audio.get_wav_data())

    try:
        print("Recoginizing..")
       
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Thrishaa J\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'email to trisha' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "anushaa23j@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent! ")
            except Exception as e:
                print(e)
                speak("sorry not able to send the email!")


        






