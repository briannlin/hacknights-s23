import pyttsx3

# Function to speak words
def speak(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()