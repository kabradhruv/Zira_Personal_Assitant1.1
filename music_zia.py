import os
import random
from takecommand_zia import takecommand
from speak_zia import speak

# this is to define mus_dir and songs
mus_dir = 'C://Users//ASUS//Desktop//pendrive//purane gaane dada pendrive se//New folder'
songs = os.listdir(mus_dir)

def play_music():
    speak("how would your prefer the songs \n"
          "1 from the top \n"
          "2 randomly \n"
          "1 or 2")
    print("how would your prefer the songs \n"
          "1 from the top \n"
          "2 randomly \n"
          "1 or 2")

    mus_ans = takecommand().lower()

    if "1" in mus_ans:
        os.startfile(os.path.join(mus_dir, songs[0]))

    elif "2" in mus_ans:
        mus_ran = random.randint(0, 457)
        os.startfile(os.path.join(mus_dir, songs[mus_ran]))

    else:
        print("try again by calling  play music command")
        speak("try again by calling  play music command")
    return None
