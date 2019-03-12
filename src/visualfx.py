import pygame, random

currentvfx = []

window = pygame.display.get_surface()
info = pygame.display.Info()
screenW, screenH = info.current_w, info.current_h

class vfxobj():

    def __init__(self, effect, x, y):
        self.effect = effect
        self.x = x
        self.y = screenW-y
        self.tl = 0

        if effect == "explosion":
            self.ttl = 30
    
    def update(self):
        self.tl += 1
        self.ttl += -1

        if self.ttl < 1:
            currentvfx.remove(self)

    def draw(self):
        
        if self.effect == "explosion":
            if self.tl < 10:
                pygame.draw.circle(window, (255,255,255), (self.x, self.y), int(self.tl * 3))
            
            if self.tl < 30:
                color = (255 , int(255 - (self.tl * 1.5)), int(255 - (self.tl * 5)))
                pygame.draw.circle(window, color, (self.x, self.y), int(self.tl * 1.1))


def addeffect(effect, x, y):
    currentvfx.append(vfxobj(effect, int(x), int(y)))

def run():
    for i in currentvfx:
        i.update()

def draw():
    for i in currentvfx:
        i.draw()
    


