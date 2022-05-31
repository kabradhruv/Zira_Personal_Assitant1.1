import speech_recognition as sr
from speak_zia import speak


# mic = sr.Microphone(device_index=2)
mic = sr.Microphone()


# this function allow to listen to what you have to say
def takecommand():
    query = ""
    r = sr.Recognizer()
    with mic as source:
        print("listening..")
        speak('listening')
        audio = r.listen(source)
        try:
            print("recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said : {query}\n")

        except (sr.UnknownValueError):
            sigt = "Sorry,I didn't get that"
            print(sigt)
            speak(sigt)

        except Exception as e:
            print(e)
            stg = "say that again please"
            print(stg)
            speak(stg)

    return query


