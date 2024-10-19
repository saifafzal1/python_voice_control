import os
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import speech_recognition as sr

# Set up paths
chromedriver_path = "/usr/local/bin/chromedriver"  # Update with the correct path to chromedriver
audio_file_path = Path.home() / "Documents" / "audio_files" / "audio_file.wav"  # Path to your audio file

# Check if chromedriver exists
#if not chromedriver_path.exists():
#    raise FileNotFoundError(f"Chromedriver not found at {chromedriver_path}")


# Function to use speech recognition for user input
def listen_to_voice_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Please say something...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results from the speech recognition service.")
        return None

def main():
    # Run the tests
    test_folder_path="/Users/saif.afzal/tests/OrangeHrmSuite"
   # Run the tests initially
    result = pytest.main([test_folder_path, "-v", "--disable-warnings"])

    if result == pytest.ExitCode.OK:
        print("All tests passed. Would you like to run failed tests?")
        command = listen_to_voice_command()

        if command and "yes please" in command:
            print("There are no failed tests to run.")
        else:
            print("Tests complete.")
    else:
        print("Some tests failed. Would you like to rerun them?")
        command = listen_to_voice_command()

        if command and "yes" in command:
            print("Running failed tests...")
            # Rerun the failed tests
            result = pytest.main([test_folder_path, "-v", "--disable-warnings", "--last-failed"])
            if result == pytest.ExitCode.OK:
                print("All previously failed tests passed.")
            else:
                print("Some previously failed tests still failed.")
        else:
            print("Tests complete.")

if __name__ == "__main__":
    main()