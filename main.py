import speech_recognition as sr
import pyttsx3
import subprocess
import time
import pyautogui
import pygame
import oracledb
import os

pygame.mixer.init()

def play_sound(file_path):
    """Play a sound file."""
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(4)
    except Exception as e:
        print(f"Error playing sound: {e}")

def play_sorry_what_did_you_say():
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\adu\wdd.mp3")

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
    subprocess.Popen(r"C:\Users\ZTS\AppData\Local\WhatsApp\WhatsApp.exe")

def open_spotify():
    subprocess.Popen(r"C:\Users\ZTS\AppData\Roaming\Spotify\Spotify.exe")

def play_game():
    subprocess.Popen(r"E:\Yu-Gi-Oh.Legacy.of.the.Duelist.Link.Evolution\Yu-Gi-Oh! Legacy of the Duelist Link Evolution\YuGiOh.exe")

def user_info():
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\users info\you_know_who_im.mp3")   


def play_music():
    """Play music in Spotify."""
    open_spotify()
    play_here_is_your_mus()
    time.sleep(3)
    pyautogui.press('space')
    print("Music started on Spotify.")

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    try:
        tts_engine.runAndWait()
    except KeyboardInterrupt:
        print("Speech interrupted.")
def get_valid_microphone_index():
    """Select a valid microphone index dynamically."""
    mic_list = sr.Microphone.list_microphone_names()
    
    if not mic_list:
        print("No microphones found.")
        return None

    print("Available Microphones:")
    for i, mic_name in enumerate(mic_list):
        print(f"{i}: {mic_name}")

    # Loop through microphones to find a valid input device
    for index, mic_name in enumerate(mic_list):
        if "microphone" in mic_name.lower() or "input" in mic_name.lower():
            print(f"Using: {mic_name} (Index: {index})")
            return index  # Return the first valid microphone

    print("No valid microphone found.")
    return None

def listen_for_20_seconds():
    """Listen for speech input for up to 20 seconds."""
    device_index = get_valid_microphone_index()
    if device_index is None:
        print("No available microphone to use.")
        return ""

    try:
        with sr.Microphone(device_index=device_index) as source:
            print("Listening for 20 seconds...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=20)
            print("Processing your input...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
    except AttributeError as e:
        print(f"Error accessing microphone: {e}")
        return ""
    except sr.UnknownValueError:
        play_sorry_what_did_you_say()
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
            print(f"Sorry, I don't know how to open {app_name}.")
    except Exception as e:
        print(f"Error opening app: {e}")
        speak("I couldn't open the application.")

def sleep_pc():
    """Put the computer to sleep."""
    subprocess.run(r"C:\Windows\System32\rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def main():
    attempts = 3
    for _ in range(attempts):
        user_input = listen_for_20_seconds()
        if user_input:
            if "hi" in user_input or "hello" in user_input:
                play_greeting()
                print("Hello! How are you?")
            elif any(word in user_input for word in ["bye", "boy"]):
                play_cya()
                print("cya")
            elif "shut down" in user_input or "turn off" in user_input:
                sleep_pc()
            elif "play" in user_input:
                app_name = user_input.replace("play", "").strip()
                if "game" in app_name:
                    play_game()
            elif "open" in user_input:
                app_name = user_input.replace("open", "").strip()
                if "spotify" in app_name:
                    play_music()
                elif "whatsapp" in app_name:
                    open_whatsapp()
            elif "what do you know about" in user_input:
                app_name = user_input.replace("describe", "").strip()  
                if "muhammad" in app_name:  
                    user_info()
                else:
                    print("I don't know this person.")
            else:
                speak("I didn't understand. Can you repeat?")
            break
        else:
            speak("I didn't catch that. Let's try again.")
    else:
        print("Max attempts reached.")

if __name__ == "__main__":
    main()
