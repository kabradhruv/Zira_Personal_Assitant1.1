import datetime
from speak_zia import speak
# this function is to wish me when the program starts
def wishme():
    speak("Initializing Jarvis",250)
    speak("Starting all systems applications",250)
    speak("Installing and checking all drivers",250)
    speak("Caliberating and examining all the core processors",250)
    speak("Checking the internet connection",250)
    speak("Wait a moment sir",250)
    speak("All drivers are up and running",250)
    speak("All systems have been activated",250)
    speak("Now I am online")
    dttosay = datetime.datetime.now().strftime("%A %I %M %p")
    dttosay = dttosay.replace("0", "")
    hour = int(datetime.datetime.now().hour)
    if hour <= 0 and hour >= 12:
        speak("good morning sir")
    elif hour <= 12 and hour >= 16:
        speak("good evening sir")
    else:
        speak("good afternoon sir")
    speak(f"i am David your personal assistant its {dttosay} please tell me how may i help you")
    return None
