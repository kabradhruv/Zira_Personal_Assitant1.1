# all importing modules
import os
import wikipedia
import webbrowser
import datetime

# all modules from different directories importing here
from speak_zia import speak
from takecommand_zia import takecommand
from wishme_zia import wishme
from automatic_email_sender_forgit.automatic_email_sender import get_email_info

# this line is to set chrome as a default web browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C://Users//ASUS//AppData//Local//Google//Chrome//Application//chrome.exe"))
c = webbrowser.get('chrome')

#defining list
cal = ["calculator", "calci", "calculation"]

# our main program starts from here
if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            wikipedia_source = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(wikipedia_source, sentences=1)
                speak("according to wikipedia")
                print(results)
                speak(results)
                print("Sir,Do you want to know more?..")
                speak("Sir,Do you want to know more?")
                query=takecommand()
                if "yes" in query:
                    results = wikipedia.summary(wikipedia_source, sentences=5)
                    speak("according to wikipedia")
                    print(results)
                    speak(results)

                elif "no" in query:
                    print("Ok,Sir")
                    speak("Ok,Sir")

                else:
                    pass
            except wikipedia.exceptions.DisambiguationError:
                print("Sir,Please be more accurate")
                speak("Sir,Please be more accurate")
            except Exception as e:
                print(e)
                speak("Sorry sir failed to fetch data.try again")

        elif "open youtube" in query:
            print("opening youtube")
            speak("opening youtube")
            c.open("youtube.com")

        elif "open google" in query:
            print("opening google")
            speak("opening google")
            c.open("google.com")

        elif "open facebook" in query:
            print("opening facebook")
            speak("opening facebook")
            c.open("facebook.com")

        elif "open instagram" in query:
            print("opening instagram")
            speak("opening instagram")
            c.open("instagram.com")

        elif "open twitter" in query:
            print("opening twitter")
            speak("opening twitter")
            c.open("twitter.com")

        elif "open stack overflow" in query:
            print("opening stack overflow")
            speak("opening stack overflow")
            c.open("stackoverflow.com")


        elif query in cal:
            os.system("C:\\Windows\\System32\\calc.exe")
            # print("This will be hard to work in speech recognition,so it will speak but take input from keyboard:")
            # speak("This will be hard to work in speech recognition,so it will speak but take input from keyboard")
            # from all_calculato_zira.calculator_zira import calculator
            # calculator()

        elif query in ["music", "muzic", "play music"]:
            from music_zia import play_music

            play_music()

        elif query in ["thank you", "ty", "that is all"]:
            tyibp = "thank you sir it's been pleasure working for you"
            print(tyibp)
            speak(tyibp)
            break

        elif query in ["pycharm", "vscode", "code", "python"]:
            from opencodecommand_zia import oppycode

            oppycode()

        elif query in ["time", "what is the time", "clock", "what time is it"]:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")

        elif query in ['send mail','send email',"send a mail"] :
            get_email_info()

        else:
            speak("Sorry")
            speak("did'nt get what you are trying to say",200)
