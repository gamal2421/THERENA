import subprocess
import time
import webbrowser
import pyautogui
import os

from sounds import play_here_is_your_mus
def open_chrome(search_query=""):
    """Open Google Chrome and optionally perform a search."""
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Adjust path if needed

    if os.path.exists(chrome_path):
        if search_query:
            # Format search query into a Google search URL
            url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
            # Use Chrome to open the search URL
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        else:
            # Just open Chrome without a search if no query is provided
            subprocess.Popen(chrome_path)
    else:
        print("Chrome not found.")




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






def open_whatsapp():
    """Open WhatsApp desktop application."""
    whatsapp_path = r"C:\Users\ZTS\AppData\Local\WhatsApp\WhatsApp.exe"
    if os.path.exists(whatsapp_path):
        subprocess.Popen(whatsapp_path)

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
        elif "whatsapp" in app_name.lower():
            open_whatsapp()
        elif "chrome" in app_name.lower() or "google" in app_name.lower():
            open_chrome()
        else:
            print(f"Sorry, I don't know how to open '{app_name}'.")
    except Exception as e:
        print(f"Error opening app: {e}")
