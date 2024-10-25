import pygame
pygame.mixer.init()
def play_sound(file_path):
    """Play a sound file."""
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(4)
        pygame.mixer.music.unload()
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
def muhammad_info():
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\users info\you_know_who_im.mp3")
def hala_info():
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\users info\bos_ya_bos.mp3")
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\users info\meeeees.mp3")
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\users info\moaz_min.mp3")
    play_sound(r"C:\Users\ZTS\Desktop\ai for school\users info\the_first_3_bons.mp3")
