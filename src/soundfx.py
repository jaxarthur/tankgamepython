import pygame, random, time, queue, threading

sfxqueue = queue.Queue(0)

def sfxthread():
    while True:
        while not sfxqueue.empty():
            filepath, volume = sfxqueue.get()
            sound = pygame.mixer.Sound(filepath)
            sound.set_volume(volume)
            sound.play()
        
def queuesfx(file, volume):
    fullpath = "resources/sounds/effects/" + file
    sfxqueue.put([fullpath, volume])


def init():
    thread = threading.Thread(target=sfxthread)
    thread.start
