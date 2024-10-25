import speech_recognition as sr
import pyttsx3
import time
import pyautogui

# Importing custom modules
from sounds import *
from sp_rec import listen_for_20_seconds
from open import *

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    try:
        tts_engine.runAndWait()
    except KeyboardInterrupt:
        print("Speech interrupted.")

def main():
    the_ai_name = "Therena"
    print(f"{the_ai_name} is listening...")
    try:
        user_input = listen_for_20_seconds()
        print(f"You said: {user_input}")
        if not user_input:
            speak("I didn't catch that. Let's try again.")
            return
        if "hi" in user_input or "hello" in user_input:
            play_greeting()
            print("Hello! How are you?")
        elif any(word in user_input for word in ["bye", "boy", "goodbye"]):
            play_cya()
            print("Goodbye!")
        elif "shut down" in user_input or "turn off" in user_input:
            sleep_pc()

        elif "play" in user_input:
            app_name = user_input.replace("play", "").strip()
            if "game" in app_name:
                play_game()
            elif "music" in app_name:
                play_music()

        elif "open" in user_input:
            app_name = user_input.replace("open", "").strip()
            open_app(app_name)

        elif "what do you know about" in user_input:
            person = user_input.replace("what do you know about", "").strip()
            if "muhammad" in person:
                muhammad_info()
            elif "hala" in person or "hela" in person:
                hala_info()
            elif "ntg" in person:
                speak("NTG Clarity Networks is a technology company focused on providing solutions and services ")
            else:
                print("I don't know this person.")

        else:
            print("I didn't understand that.")

    except Exception as e:
        print(f"An error occurred: {e}")

main()
