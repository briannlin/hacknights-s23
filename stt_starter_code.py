# FROM: https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py

import speech_recognition as sr

# Create an instance of Recognizer, which acts as an interface providing speech recognition functionality.
r = sr.Recognizer()

# Enter a loop to start recognizing lines of speech punctuated by a pause.
while True:
    try:
         # Obtain audio using your computer's default microphone as an audio source.
        with sr.Microphone() as source:
            print("Say something!")

            # Adjust and account for the ambient noise levels picked up by the microphone.
            r.adjust_for_ambient_noise(source)

            # Listen and pick up mic audio until you pause, or after 10 seconds has passed.
            audio = r.listen(source, phrase_time_limit=10)

            # Perform text-to-speech recognition on the audio.
            text = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + text)

            # If "quit" is recognized in the audio, quit the program.
            if ("quit" in text):
                print("Goodbye! ( • ͜ •)7")
                quit(0);

    # Catch exceptions and handle them by creating a new instance of the Recognizer interface.
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        r = sr.Recognizer()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        r = sr.Recognizer()