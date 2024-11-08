import subprocess
import time
import pyautogui
import os

from sounds import play_here_is_your_mus
def open_chrome():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  
    subprocess.Popen(chrome_path)

def open_search_google(user_input):
    open_chrome()
    time.sleep(5)
    pyautogui.write(user_input)
    pyautogui.press('enter')  





def play_music():
    """Play music in Spotify."""
    try:
        play_here_is_your_mus()
        open_spotify()
        time.sleep(3)  # Allow some time for the app to load
        pyautogui.press('space')  # Simulate pressing the play button
        print("Music started on Spotify.")
    except Exception as e:
        print(f"Error starting music: {e}")







def open_spotify():
    """Open Spotify application."""
    spotify_path = r"C:\Users\ZTS\AppData\Roaming\Spotify\Spotify.exe"
    if os.path.exists(spotify_path):
        subprocess.Popen(spotify_path)

def play_game():
    """Open the Yu-Gi-Oh! game."""
    game_path = r"E:\Yu-Gi-Oh.Legacy.of.the.Duelist.Link.Evolution\Yu-Gi-Oh! Legacy of the Duelist Link Evolution\YuGiOh.exe"
    if os.path.exists(game_path):
        subprocess.Popen(game_path)
   
   

def sleep_pc():
    """Put the computer to sleep."""
    try:
        subprocess.run(r"C:\Windows\System32\rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    except Exception as e:
        print(f"Failed to put the computer to sleep: {e}")


def open_app(app_name):
    """Open an application based on the provided name."""
    try:
        if "spotify" in app_name.lower():
            play_music()
        elif "chrome" in app_name.lower() or "google" in app_name.lower():
            search_for = app_name.replace("chrome and search for", "").strip()
            open_search_google(search_for)
        else:
            print(f"Sorry, I don't know how to open '{app_name}' so i search for it on your pc.")
            pyautogui.press('winright')
            pyautogui.write(app_name)
            time.sleep(2)
            pyautogui.press('enter')
    except Exception as e:
        print(f"Error opening app: {e}")