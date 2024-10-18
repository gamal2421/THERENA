import speech_recognition as sr
import pyttsx3
import os
import subprocess
import time
import pyautogui
import pygame
import ctypes   

pygame.mixer.init()

def play_sound(file_path):
    """Play a sound file."""
    try:
        pygame.mixer.music.load(file_path)  # Load your audio file
        pygame.mixer.music.play()  # Play the audio
        # Wait until the sound finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(4)
    except Exception as e:
        print(f"Error playing sound: {e}")



def play_here_is_your_mus():
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\adu\here is your nigga.mp3")
def play_cya():
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\adu\cya.mp3")
def play_greeting():
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\adu\hello.mp3")

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def open_whatsapp():
    subprocess.Popen(r"C:\Users\ZTS\AppData\Roaming\Spotify\Spotify.exe")
def open_spotify():
    subprocess.Popen(r"C:\Users\ZTS\AppData\Roaming\Spotify\Spotify.exe")



def play_music():
    """Play music in Spotify."""
    open_spotify()
    play_here_is_your_mus()
    time.sleep(3)  
    pyautogui.press('space') 
def speak(text):
    """Convert text to speech."""
    tts_engine.say (text)
    tts_engine.runAndWait()
    time.sleep(1)
def listen_for_20_seconds():
    """Listen for speech input for up to 20 seconds."""
    with sr.Microphone(device_index=3) as source:
        print("Listening for 20 seconds...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        try:
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=20)
            print("Processing your input...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError:
            print("Request failed; please check your network.")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            return ""
        






def open_app(app_name):
    """Open an application based on the name."""
    try:
        if "spotify" in app_name:
            play_music()
        else:
            speak(f"Sorry, I don't know how to open {app_name}.")
    except Exception as e:
        print(f"Error opening app: {e}")
        speak("I couldn't open the application.")

def sleep_pc():
    """Put the computer to sleep."""
##sleep sound from blal
    print("Executing sleep command...")
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



def main():
    attempts = 3 
    for _ in range(attempts):
      ##  print(sr.Microphone.list_microphone_names()) this just for testing the mic
        user_input = listen_for_20_seconds()
        if user_input:

            if "hi" in user_input or "hello"  in user_input:
                play_greeting()
                speak("Hello! How are you?")
            elif any(word in user_input for word in ["bye", "boy"]):
                play_cya()
                speak("Goodbye!")


            elif "shut down" in user_input or "turn off" in user_input:
                sleep_pc() 


            elif "open" in user_input:
                app_name = user_input.replace("open", "").strip()
                if "music" in user_input:
                    play_music()
                elif "whatsapp" in user_input:
                    open_whatsapp()
                else:
                    open_app(app_name)




            else:
                speak("I didn't understand. Can you repeat?")
            break 
        else:
            speak("I didn't catch that. Let's try again.")
if __name__ == "__main__":
    main()
