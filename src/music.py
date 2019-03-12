import pygame, threading, random

musicfiles = ["music1.wav"]

def musicthread():
    while True:
        if not pygame.mixer.music.get_busy():
            music = musicfiles[random.randint(0, len(musicfiles)-1)]
            pygame.mixer.music.load(music)
            pygame.mixer.music.play(1)

def init():
    global musicfiles
    tempfilenames = []

    for mfile in musicfiles:
        tempfilenames.append("resources/sounds/music/"+mfile)

    musicfiles = tempfilenames

    thread = threading.Thread(target=musicthread)
    thread.start()