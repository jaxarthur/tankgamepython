import pygame, math, random, time
from classes import *
sw, sh = 600, 400

#variables
listofbullets = []
listoftanks = []
running = True
playerlocation = (0, 0)
playerturn = True

#pygame objects
win = pygame.display.set_mode((wScreen,hScreen))
bulletimg = pygame.image.load("bullet1.png")
tankimg = pygame.image.load("tank.png")
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load('music.wav')
#pygame.mixer.music.play(-1)

def AIaim(location):
    offset = location[0] - playerlocation[0]
    angle = offset / 1200 * 90
    randangle = angle + random.randint(-10, 10)
    return [randangle, 50]

#bulletform x y motionx motiony
def createbullet(typeofbullet, x, y, mx, my):
    listofbullets.append([typeofbullet, x, y, mx, my])

def updatebullets():
    if len(listofbullets) > 0:
        for i, bullet in enumerate(listofbullets):
            #update position based on motion
            bullet[1] = bullet[1] + bullet[3] * physicsscale
            bullet[2] = bullet[2] - bullet[4] * physicsscale
            #update motion
            bullet[3] = bullet[3] / dragmultiplyer
            bullet[4] = bullet[4] - gravitymultiplyer
            #restrict motion
            if terminalvelocity < bullet[4]:
               bullet[4] = terminalvelocity
            #check for out of bounds
            if wScreen < bullet[1] or bullet[1] < 0 or hScreen <bullet[2] or bullet[2]< 0:
                print('del')
                del listofbullets[i]

def drawbullets():
    if len(listofbullets) > 0:
        for i, bullet in enumerate(listofbullets):
            typeofbullet, x, y, mx, my= bullet
            rotation = math.degrees(math.atan2(my, mx))
            render1 = pygame.transform.rotate(bulletimg, rotation - 90)
            render2 = pygame.transform.smoothscale(render1, (20, 20))
            #print(render2)
            win.blit(render1, (x, y))

#tank layout type color x y turret info(angle,power)
def createtank(typeoftank, color, x, y):
    listoftanks.append([typeoftank, color, x, y, [0, 1]])

def updateplayer(keys):
    if len(listoftanks) > 0:
        for i, tank in enumerate(listoftanks):
            if tank[0] == "player":
                print("checking")
                if keys[pygame.K_d] and tank[4][0] < 91:
                    tank[4][0] = tank[4][0] + 1
                if keys[pygame.K_a] and tank[4][0] > -91:
                    tank[4][0] = tank[4][0] - 1
                if keys[pygame.K_w] and tank[4][1] < 101:
                    tank[4][1] = tank[4][1] + 1
                if keys[pygame.K_s] and tank[4][1] > 0:
                    tank[4][1] = tank[4][1] - 1
                playerlocation = tank[4]
                print(tank[4])
                print(math.cos(math.radians(tank[4][0])) * tank[4][1], math.sin(math.radians(tank[4][0])) * tank[4][1])
                if keys[pygame.K_f]:
                    return True
                else:
                    return False

def updateenemys():
    if len(listoftanks) > 0:
        for i, tank in enumerate(listoftanks):
            if tank[0] == "enemy":
                tank[4] = AIaim((tank[2], tank[3]))

def drawtanks():
    if len(listoftanks) > 0:
        for i, tank in enumerate(listoftanks):
            win.blit(tankimg, (tank[2], tank[3]))

def endturn():
    if len(listoftanks) > 0:
        for i, tank in enumerate(listoftanks):
            createbullet(tank[0], tank[2], tank[3], math.sin(math.radians(tank[4][0])) * tank[4][1], math.cos(math.radians(tank[4][0])) * tank[4][1])

createtank("player", (0), 100, 500)
createtank("enemy", (), 500, 500)
createtank("enemy", (), 900, 500)
drawtanks()

while running:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if(playerturn) :
        if updateplayer(pygame.key.get_pressed()):
            playerturn = False
    else:
        updateenemys()
        endturn()
        playerturn = True

    updatebullets()
    drawbullets()
    drawtanks()
    pygame.display.flip()
    clock.tick(10)

pygame.quit()