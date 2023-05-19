# FROM: https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py

import speech_recognition as sr
import random
import pyttsx3
import os
import time

# Function to speak words
def speak(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

# Create an instance of Recognizer, which acts as an interface providing speech recognition functionality.
r = sr.Recognizer()

# List of cringe words
cringe = ["league", "valorant", "league of legends", "computer science and engineering", "cse"]

# List of pog words
pog = ["among us", "floof", "hack", "venus hacks", "uci"]

# List of responses

responses = ["cool", "okay okay", "interesting", "nice", "keep going", "oh wow", "nice"]

# Rizz Points

rizz_points = 3

# Enter a loop to start recognizing lines of speech punctuated by a pause.
while True:
    try:
         # Obtain audio using your computer's default microphone as an audio source.
        with sr.Microphone() as source:
            print("Listening...")

            # Adjust and account for the ambient noise levels picked up by the microphone.
            r.adjust_for_ambient_noise(source)

            # Listen and pick up mic audio until you pause, or after 10 seconds has passed.
            audio = r.listen(source, phrase_time_limit=10)

            # Perform text-to-speech recognition on the audio.
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said: " + text)

            detected = False

            # If "hello" is recognized in the audio, quit the program.
            if ("hello" in text):
                print("Hi! ( • ͜ •)7")
                speak("Hi!")
                

            # If "quit" is recognized in the audio, quit the program.
            if ("bye" in text):
                print("Goodbye! ( • ͜ •)7")
                speak("Goodbye!")
                quit(0)

            # If cringe is recognized in the audio, lose rizz points.
            for word in cringe:
                if (word in text):
                    print("Uhhhh weird but ok, let's change topic (╥﹏╥)")
                    speak("Uhhhh weird but ok, let's change topic")
                    rizz_points-=1
                    detected = True

            # If pog is recognized in the audio, gain rizz points.
            for word in pog:
                if (word in text):
                    print("Wait that's amazing! (♥_♥)")
                    speak("Wait that's amazing!")
                    detected = True
                    rizz_points+=1

            if detected == False:
                the_response = random.choice(responses)
                print(the_response, "( • ͜ •)")
                speak(the_response)
                

            
            print(f"RIZZ POINTS: {rizz_points}/5")

            time.sleep(5)
            os.system('CLS')

            if rizz_points >= 5:
                speak("I really enjoyed our date! Here's my number: 9717774546, let's meet again soon! ")
                print("I really enjoyed our date! Here's my number: 9717774546, let's meet again soon! (✿ ♥‿♥) " )
                quit(0)

            if rizz_points <= 0:
                speak("Sorry I'm not enjoying this, please never contact me again!")
                print("Sorry I'm not enjoying this, please never contact me again! (✖╭╮✖)" )
                quit(0)


            

    # Catch exceptions and handle them by creating a new instance of the Recognizer interface.
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        r = sr.Recognizer()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        r = sr.Recognizer()