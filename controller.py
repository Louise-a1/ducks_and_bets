import pygame

from Duck import *
from view import *

pygame.init()

def controller():

    d = Duck(5, 5, 150, 150)

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
            d.set_direction("left")

        elif keys[pygame.K_RIGHT] and d.x < 1900 - d.width - d.vel:
            d.set_direction("right")

        elif keys[pygame.K_UP] and d.y > 4:
            d.set_direction("up")

        elif keys[pygame.K_DOWN] and d.y < 1000:
            d.set_direction("down")

        else:
            d.set_direction("standing")

        # bet
        if keys[pygame.K_b]:
            d.duck_bet()

        # quit
        if keys[pygame.K_q]:
            run = False

        # check for map changes
        d.set_map()

        redraw_view(d)



controller()