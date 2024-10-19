import speech_recognition as sr

recognizer = sr.Recognizer()

def speech_to_text():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your speech...")

        try:
            # Set timeout to 5 seconds and phrase time limit to 10 seconds
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for speech.")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Request to Google Web Speech API failed.")

if __name__ == "__main__":
    speech_to_text()

