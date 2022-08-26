from operator import truediv
import pygame
from pathlib import Path

from Duck import *

bg = pygame.image.load(Path("art/maps/map_alpha_1.jpg"))
dimg_left = pygame.image.load(Path("art/duck-1/duck_alpha_1_left.png"))
dimg_right = pygame.image.load(Path("art/duck-1/duck_alpha_1_right.png"))

d = Duck(5, 5, 150, 150)

pygame.init()


win = pygame.display.set_mode((1900, 1020))
# win = pygame.display.set_mode((0, 0), pygame.RESIZABLE) # pygame.FULLSCREEN

pygame.display.set_caption("Walk Simulator")


def redraw_view(duck):
    win.fill((10, 20, 30))
    win.blit(bg, (0, 0))

    if duck.left == True:
        win.blit(dimg_left, (duck.x,duck.y))
    elif duck.right == True:
        win.blit(dimg_right, (duck.x,duck.y))
    # pygame.draw.rect(win, (100, 150, 100), (duck.x, duck.y, duck.width, duck.height)) -- > pygame rectangle, colors with rgb and positioning
    pygame.display.update()



def controller():

    clock = pygame.time.Clock()
    run = True
    # mainloop
    while run:
        clock.tick(40)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # move Player
        if keys[pygame.K_LEFT] and d.x > d.vel:
            d.x -= d.vel
            d.left = True
            d.right = False
        elif keys[pygame.K_RIGHT] and d.x < 1900 - d.width - d.vel:
            d.x += d.vel
            d.left = False
            d.right = True
        elif keys[pygame.K_UP] and d.y > 4:
            d.y -= d.vel
        elif keys[pygame.K_DOWN] and d.y < 1000:
            d.y += d.vel

        redraw_view(d)



controller()