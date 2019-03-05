import pygame, math, random, time
pygame.init()
window = pygame.display.set_mode((800,800))
import bullet, tank, terrain


running = True

clock = pygame.time.Clock()

tank.createtank("player", 50)

tank.createtank("computer", 400)

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
    clock.tick(60)

pygame.quit()