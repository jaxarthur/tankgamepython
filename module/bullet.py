import math, pygame, tank, terrain

window = pygame.display.get_surface()
info = pygame.display.Info()
screenW, screenH = info.current_h, info.current_w
bulletlist = []
bulletimg = pygame.image.load("../resources/images/bullet.png")

class bullet():
    gravity = 1
    
    def __init__(self, x, y, mx, my, owner, typeofbullet):
        self.x, self.y, self.mx, self.my, self.owner, self.type = x, y, mx, my, owner, typeofbullet
        
    def move(self):
        self.x = self.x + self.mx
        self.y = self.y + self.my

    def physics(self):
        self.my = self.my - self.gravity

    def deletebullet(self):
        terrain.land.deform((self.x, self.y), 10)
        tank.damage(self.x, self.y, 10)
        del self

    def outofbounds(self):
        if self.x > screenW or self.x < 0 or terrain.land.colisiondetect((self.x, self.y)):
            self.deletebullet()

    def draw(self):
        angle = math.degrees(math.tan(self.my/self.mx))
        temp = pygame.transform.rotate(bulletimg, angle)
        window.blit(temp, (self.x, self.y))
        
def createbullet(x, y, mx, my, owner, typeofbullet):
    bulletlist.append(bullet(x, y, mx, my, owner, typeofbullet))

def run():
    for thing in bulletlist:
        thing.move()
        thing.physics()
        thing.outofbounds()

def draw():
    for thing in bulletlist:
        thing.draw()