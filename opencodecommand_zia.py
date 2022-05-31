import os
from speak_zia import speak
from takecommand_zia import takecommand


# this function is used to open pycharm
def oppycode():
    codepathpycharm = "C://Program Files//JetBrains//PyCharm Community Edition 2021.1.1//bin//pycharm64.exe"
    codepathvscode = "C://Users//ASUS//AppData//Local//Programs//Microsoft VS Code.exe"
    speak("what should i open \n"
          "1 pycharm \n"
          "2 vs code \n"
          "1 or 2")
    print("what should i open :\n"
          "1 pycharm \n"
          "2 VS code \n"
          "1 or 2")
    code_answer = takecommand().lower()
    if "1" in code_answer:
        os.startfile(codepathpycharm)
        print("Opening pycharm")
        speak("Opening pycharm")

    elif "2" in code_answer:
        os.startfile(codepathvscode)
        print("Opening VScode")
        speak("Opening vscode")

    else:
        print("try again by calling open code")
        speak("try again by calling open code")
    return None
