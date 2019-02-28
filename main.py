import pygame, math, random, time
import module.bullet, module.tank, module.terrain

sw, sh = 600, 400

running = True

window = pygame.display.set_mode((480,360))
clock = pygame.time.Clock()

while running:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    module.tank.run()
    module.bullet.run()

    module.tank.draw()
    module.bullet.draw()

    pygame.display.flip()
    clock.tick(10)

pygame.quit()