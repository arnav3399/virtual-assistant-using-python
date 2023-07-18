import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import speech_recognition.exceptions as sr_exceptions

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'rose' in command:
                command = command.replace('rose', '')
                print(command)
    except sr_exceptions.WaitTimeoutError:
        print('Timeout error occurred.')
        return None
    except sr_exceptions.UnknownValueError:
        print('Unable to recognize speech.')
        return None
    except sr_exceptions.RequestError:
        print('Speech recognition service is unavailable.')
        return None
    except Exception as e:
        print('An error occurred:', str(e))
        return None
    return command


def run_rose():
    command = take_command()
    print(command)
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say the command again.')


while True:
    run_rose()
