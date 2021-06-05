import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

hour = int(datetime.datetime.now().hour)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    if hour >= 0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour >= 12 and hour <18:
        print("Good Afternoon!")
        speak("Good Afternoon! ")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("I am Eldrom, made by elderny1 from telegram please tell me how may i help you\n")
    speak("I am Eldrom, made by elderny1 from telegram please Tell me how may i help you")


def takeCommand():
    # it takes Microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening master...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing master...")
        query = r.recognize_google(audio, language='en-us')
        print(f"Master elderny said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again Please...")
        return "None"
    return query

def sendEmail(to, content):
    with open("D:\\Python\\Pycharm\\PyCharm Community Edition 2021.1.1\\jbr\\conf\\management\\passwordd.txt") as f:
        a = f.read()
    with open("D:\\Python\\Pycharm\\PyCharm Community Edition 2021.1.1\\jbr\\conf\\security\\policy\\limited\\emaill.txt") as f:
        b = f.read()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(b, a)
    server.sendmail(b, to, content)
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing taks based on query
        if 'wikipedia' in query:
            speak("Searching in elderny internet...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to mister elderny,")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak("I'm good as i'm made by elderny. Hmmmmmm")


        elif 'thanks eldrom' in query or 'eldrom' in query or 'eldrom listen' in query or 'eldrom hi' in query:
            speak("I'm here with you master")

        elif 'who are you' in query or 'who you' in query:
            speak("I'm an thing made by elderny huh")

        elif 'tell me a joke' in query or 'i want a joke' in query or 'speak a joke' in query or 'tell any joke' in query or 'tell me a joke again' in query:
            speak(pyjokes.get_joke())

        elif 'why you' in query or 'look at you' in query or 'why are you' in query:
            speak("What the fuck, you got no manners you want to get hacked? type hack me if yes")
            print("Type hack me to continue")
            ask = input().lower()
            if ask == 'hack me':
                print("I forgive you shit!")
                speak("I forgive you shit!")
                speak("Type hack if you want to get hacked like real!, or press enter to skip you noob")
                ask_advance = input("Type hack if you want to get hacked like real!, or press enter to skip you noob")
                if ask_advance == 'hack':
                    for i in range(1000):
                        i += 1
                        webbrowser.open("https://www.eldernyweb.com")


        elif 'f*** you' in query:
            speak("I'm fucking myself! hehehehehe")

        elif 'what the f***' in query:
            speak("What, you want to die")

        elif 'you shit' in query or 'you are shit' in query:
            speak("I'm hacking your system now HAHAHAHA")
            print("Installing VirusBlam")
            print("Installation Done")
            speak("Hack loaded, now elderny has full-access to your system")
            webbrowser.open("https://www.whatismyip.com/")
            webbrowser.open("https://www.shockapart.com")
            speak("I'm closing myself")
            exit()

        elif 'bastard' in query:
            speak("No, you are bastard. HAHA sorry")

        elif 'you want to die' in query:
            speak("I'm an AI you can't kill me, aye boi")

        elif 'open youtube' in query:
            speak("Opening YouTube for you my master")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google for you my master")
            webbrowser.open("google.com")

        elif 'open github' in query:
            speak("Opening github for you my master")
            webbrowser.open("github.com")

        elif 'play lofi music' in query or 'lofi music' in query or 'lofi music' in query or 'lofi' in query:
            speak("Playing lofi music online, time to chill")
            webbrowser.open("https://www.youtube.com/watch?v=DWcJFNfaw9c")

#         You need to have that folder otherwise it will throw error
#         elif 'play music' in query or 'play pc music' in query or 'play saved music' in query:
#             music_dir = 'C:\\Users\\Elderny\\Desktop\\Songs'
#             songs = os.listdir(music_dir)
#             print(songs)
#             os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'my favourite song' in query or 'play song' in query or 'play any song' in query or 'play my favourite song' in query or 'favourite song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Mlq9jrXbEFo")
            speak("Music windows opened, master elderny")
            speak("Press enter to let me listen again hehe, guru")
            print("PRESS ENTER TO SPEAK AGAIN!")
            input()

        elif 'the time' in query or 'whats the time' in query or 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The Time is {strTime}")

        elif 'open vscode' in query or 'vscode' in query or 'html editor' in query:
            codePath = "C:\\Users\\Elderny\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio code Application, master")

        elif 'open cmd' in query or 'cmd' in query:
            PycharmPath = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(PycharmPath)
            speak("Opening Cmd panel, master elderny")

        elif 'open pycharm' in query or 'open code editor' in query or 'open python editor' in query or 'python editor' in query or 'good coding app' in query:
            PycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.1\\bin\\pycharm64.exe"
            os.startfile(PycharmPath)
            speak("Opening Coding Application, master")

        elif 'email to me' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "eldernytech@gmail.com"
                sendEmail(to, content)
                print("Email has been sent")
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry my friend elderny, I'm not able to send this")
        print("\nI'm Listening AGAIN!")

        if 'stop' in query or 'stop it' in query or 'stop yourself' in query:
            speak("Sorry, Im stopped now, press enter to resume me")
