import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


listener =sr.Recognizer()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.......')
            voice =listener.listen(source)
            command =listener.recognize_google(voice)
            if 'jarvis' in command:
                command =command.replace('jarvis','')
                print(command)
            

    except:
        pass
    return command
def run_jarvis():
    command =take_command()
    print(command)
    if 'play' in command:
        song =command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time =datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'who is ' in command:
        person =command.replace('who is ','')
        info =wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'what is' in command:
        data = command.replace('what is','')
        info=wikipedia.summary(data,2)
        print(info)
        talk(info)
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    else : 
        talk('Please say the command again')
while True:      
    run_jarvis()
