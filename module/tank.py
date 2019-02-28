import math, pygame, random, bullet, terrain

window = pygame.display.get_surface()
info = pygame.display.Info()
screenW, screenH = info.current_h, info.current_w

tankimgp = pygame.image.load("../resources/images/playertank.png")
tankimgc = pygame.image.load("../resources/images/enemytank.png")
turretimgp = pygame.image.load("../resources/images/playerturret.png")
turretimgc = pygame.image.load("../resources/images/enemyturret.png")

playerx, playery = 0,0
tanklist = []

class tank():
    def __init__(self, typeofplayer, x):
        tempx, tempy = terrain.land.find(x)
        self.typeofplayer, self.x, self.y = typeofplayer, tempx, tempy
        self.ready = False
        self.angle = 0
        self.power = 50
        self.health = 100

    def gravity(self):
        if self.y < terrain.land.find(self.x):
            self.y = self.y - 1
        elif self.y > terrain.land.find(self.x):
            self.y = self.y + 1
        
    def process(self):
        if self.typeofplayer == "player":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.power = self.power + 1
            if keys[pygame.K_s]:
                self.power = self.power - 1
            if keys[pygame.K_d]:
                self.angle = self.angle + 1
            if keys[pygame.K_a]:
                self.angle = self.angle - 1
            if self.power > 100:
                self.power = 100
            if self.power < 0:
                self.power = 0
            if self.angle > 90:
                self.angle =90
            if self.angle < -90:
                self.angle = -90
            
            playerx, playery = self.x, self.y
            
            if keys[pygame.K_f]:
                self.ready = True
            
        elif self.typeofplayer == "computer":
            self.power, self.angle == aiprocess(self.x, self.y, playerx, playery)
            self.ready = True

    def fire(self):
        mx = math.sin(math.radians(self.angle))*self.power
        my = math.cos(math.radians(self.angle))*self.power
        bullet.createbullet(self.x, self.y, mx, my, self.typeofplayer, "basic")
        self.ready = False

    def damage(self, hp):
        self.health = self.health - hp
        if self.health < 1:
            self.die()

    def die(self):
        del self

    def draw(self):
        if self.typeofplayer == "player":
            temp1 = tankimgp
            temp2 = turretimgp
        else:
            temp1 = tankimgc
            temp2 = turretimgc
        
        temp2 = pygame.transform.rotate(temp2, self.angle)

        window.blit(temp1, self.x, self.y)
        window.blit(temp2, self.x, self.y-2)


    
def aiprocess(x, y, px, py):
    offsetx = x - px
    offsety = y - py
    angle = offsetx/25 + random.randint(-5,5)
    power = 20 + offsety/30
    return power, angle

def damage(x, y, r):
    for thing in tanklist:
        xoffset = x - thing.x
        yoffset = y - thing.y
        if -r**2 < (xoffset**2 + yoffset**2) < r**2:
            thing.damage(10)

def run():
    fire = True
    for thing in tanklist:
        if thing.ready == False:
            fire = False

    if fire:
        for thing in tanklist:
            thing.fire()
    else:
        for thing in tanklist:
            thing.process()
    
    for thing in tanklist:
        thing.gravity()

def draw():
    for thing in tanklist:
        thing.draw()


def createtank(typeoftank, x):
    tanklist.append(tank(typeoftank, x))

