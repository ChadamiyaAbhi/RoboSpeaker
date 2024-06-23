

import pyttsx3

# Initialize the text-to-speech engine
robo = pyttsx3.init()

while True:
    x = input("Enter what you want to pronounce (or 'q' to quit): ")
    if x.lower() == 'q':
        break
    robo.say(x)
    robo.runAndWait()
