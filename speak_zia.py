import pyttsx3

# this line is to initiate pyttsx3 module and change the speed of the voice
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


# making speak function
def speak(audio,rate=150):
    engine.setProperty('rate',rate)
    engine.say(audio)
    engine.runAndWait()
