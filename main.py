
import speech_recognition as sr
import time
"""

#audio file to text with SpeechRecognition
def audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="it-IT")
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech speech_recognitionRecognition service; {e}"

# Example usage

audio_file_path = "./tmp/paolo.wav"
print(audio_to_text(audio_file_path))
"""

def recognize_speech_from_mic():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Use the microphone as source for input
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        while True:
            audio = recognizer.listen(source)

            try:
                # Using google speech recognition
                #print("Recognizing...")
                text = recognizer.recognize_google(audio,language="it-IT")
                print(f">: {text}")
                time.sleep(0.1)
            except sr.UnknownValueError:
                print(f"[testo non riconosciuto]")
            except sr.RequestError as e:
                print(f"[non raggiungo le API Google]; {e}")

recognize_speech_from_mic()

"""
import time

import speech_recognition as sr


# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio, language="it-IT"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some unrelated computations for 5 seconds
for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

# calling this function requests that the background listener stop listening
stop_listening(wait_for_stop=False)

# do some more unrelated things
while True: time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping
"""