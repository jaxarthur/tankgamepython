import pygame, math, random, time
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((800,800))
import bullet, tank, terrain, music, soundfx

#music.init()

running = True

clock = pygame.time.Clock()

tank.createtank("player", random.randint(25, 75))

tank.createtank("computer", random.randint(350, 500))

while running:
    window.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tank.run()
    bullet.run()

    terrain.land.draw()
    tank.draw()
    bullet.draw()

    #window = pygame.transform.rotate(window, 180)
    
    pygame.display.flip()
    clock.tick(20)

pygame.quit()

quit()