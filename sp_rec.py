import speech_recognition as sr
import pyttsx3
from sounds import play_sorry_what_did_you_say

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except KeyboardInterrupt:
        print("Speech interrupted.")

def get_valid_microphone_index():
    """Select a valid microphone index dynamically."""
    mic_list = sr.Microphone.list_microphone_names()
    if not mic_list:
        print("No microphones found.")
        return None

    for index, mic_name in enumerate(mic_list):
        if "microphone" in mic_name.lower() or "input" in mic_name.lower():
            print(f"Using: {mic_name} (Index: {index})")
            return index
    print("No valid microphone found.")
    return 0
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
            return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        play_sorry_what_did_you_say()
        return ""
    except (sr.RequestError, sr.WaitTimeoutError):
        print("An error occurred while processing speech.")
        return ""