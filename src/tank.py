import math, pygame, random, bullet, terrain, time, numpy

window = pygame.display.get_surface()
info = pygame.display.Info()
screenW, screenH = info.current_w, info.current_h
tankimgp = pygame.image.load("resources/images/playertank.png")
tankimgc = pygame.image.load("resources/images/enemytank.png")
turretimgp = pygame.image.load("resources/images/playerturret.png")
turretimgc = pygame.image.load("resources/images/enemyturret.png")
font = pygame.font.SysFont("monospace", 20)

playerx, playery = 0,0
tanklist = []

class tank():
    def __init__(self, typeofplayer, x):
        tempx = x
        tempy = terrain.land.find(x)
        self.typeofplayer, self.x, self.y = typeofplayer, tempx, tempy
        self.ready = 0
        self.angle = 0
        self.power = 50
        self.health = 100

    def gravity(self):
        if self.y < 16+terrain.land.find(self.x+8):
            self.y = self.y + 1
        elif self.y > 16+terrain.land.find(self.x+8):
            self.y = self.y - 1
        
    def process(self):
        if self.ready > 0:
            self.ready -= 1
        
        if self.typeofplayer == "player":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.power = self.power + .3
            if keys[pygame.K_s]:
                self.power = self.power - .3
            if keys[pygame.K_d]:
                self.angle = self.angle + .3
            if keys[pygame.K_a]:
                self.angle = self.angle - .3
            if self.power > 100:
                self.power = 100
            if self.power < 0:
                self.power = 0
            if self.angle > 90:
                self.angle =90
            if self.angle < -90:
                self.angle = -90
            
            if keys[pygame.K_f] and self.ready == 0:
                self.ready = -1

        elif self.typeofplayer == "computer":
            if self.ready == 0:
                self.power, self.angle = aiprocess(self.x, self.y)
                self.ready = -1

    def fire(self):
        mx = math.sin(math.radians(self.angle))*self.power/2
        my = math.cos(math.radians(self.angle))*self.power/2
        bullet.createbullet(self.x+3, self.y, mx, my, self.typeofplayer, "basic")
        self.ready = 60

    def damage(self, hp):
        self.health = self.health - hp
        if self.health < 1:
            self.die()

    def die(self):
        tanklist.remove(self)

    def draw(self):
        if self.typeofplayer == "player":
            temp1 = tankimgp
            temp2 = turretimgp
            
            line1 = font.render("Power: " + str(int(self.power)) + " Angle: "+ str(int(self.angle)), True, (255,255,255))
            line2 = font.render("HP: " + str(self.health), True, (255,255,255))
            window.blit(line1, (10, 10))
            window.blit(line2, (10, 60))
        else:
            temp1 = tankimgc
            temp2 = turretimgc
        
        temp2 = pygame.transform.scale(temp2, (4, 8))
        temp3 = pygame.surface.Surface((8, 16))
        temp3.blit(temp2, (2,8))
        temp3 = pygame.transform.rotate(temp3, self.angle)
        temp3 = pygame.transform.flip(temp3, False, True)
        window.blit(temp3, (self.x+3, screenH-self.y))
        window.blit(temp1, (self.x, screenH-self.y))

    
def aiprocess(x, y):
    closest = 1000
    tempangle = 0
    temppower = 0
    for i in range(1):
        angle = random.randint(-90,90)
        power = random.randint(0,100)
        mx = math.sin(math.radians(angle))*power/2
        my = math.cos(math.radians(angle))*power/2
        simulate = simulatebullet(x, y, mx, my, playerx, playery)
        if simulate < closest:
            tempangle = angle
            temppower = power
            closest = simulate
    

    return temppower, tempangle

def simulatebullet(x, y, mx, my, tx, ty):
    bulletx = x
    bullety = y
    bulletmx = mx
    bulletmy = my
    alive = True
    while alive:
        bulletx = bulletx + bulletmx/5
        bullety = bullety + bulletmy/5
        bulletmy = bulletmy - 1/5
        if bulletx > screenW or bulletx < 0 or bullety < 0:
            alive = 0
        elif terrain.land.colisiondetect((int(bulletx), int(bullety))):
            alive = 0

    offsetx = bulletx - tx
    offsety = bullety - ty
    return(math.sqrt(math.pow(offsetx, 2)+math.pow(offsety, 2)))

def damage(x, y, r):
    for thing in tanklist:
        xoffset = x - thing.x
        yoffset = y - thing.y
        if abs(xoffset) + abs(yoffset) < 50:
            thing.damage(25)

def run():
    global playerx
    global playery
    fire = True
    for thing in tanklist:
        if thing.ready != -1:
            fire = False

    if fire:
        for thing in tanklist:
            thing.fire()
    else:
        for thing in tanklist:
            thing.process()
            if thing.typeofplayer == "player":
                playerx, playery = thing.x, thing.y

    for thing in tanklist:
        thing.gravity()

def draw():
    for thing in tanklist:
        thing.draw()


def createtank(typeoftank, x):
    tanklist.append(tank(typeoftank, x))
