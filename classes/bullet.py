import math, pygame, tank

bulletimg = pygame.image.load("../resources/images/bullet.png")

class bullet():
    gravity = 1
    
    def __init__(self, x, y, mx, my, owner, typeofbullet, screen, sw, sh):
        self.x, self.y, self.mx, self.my, self.owner, self.type, self.screen, self.sw, self.sh= x, y, mx, my, owner, typeofbullet, screen, sw, sh
        
    def move(self):
        self.x = self.x + self.mx
        self.y = self.y + self.my

    def physics(self):
        self.my = self.my - self.gravity

    def deletebullet(self, terain):
        terain.deform((self.x, self.y), 10)
        #tank.damage((self.x, self.y), 10)
        del self

    def outofbounds(self, terain):
        if self.x > self.sw or self.x < 0 or terain.colisiondetect((self.x, self.y)):
            self.deletebullet(terain)

    def draw(self, window):
        angle = math.degrees(math.tan(self.my/self.mx))
        temp = pygame.transform.rotate(bulletimg, angle)
        self.screen.blit(temp, (self.x, self.y))
        
