import pygame
from pathlib import Path

from Duck import *

home = pygame.image.load(Path("art/maps/map_alpha_12.jpg"))
house = pygame.image.load(Path("art/maps/map_alpha_2.jpg"))


dimg_left = pygame.image.load(Path("art/duck-1/duck_alpha_1_left.png"))
dimg_right = pygame.image.load(Path("art/duck-1/duck_alpha_1_right.png"))
dimg_up = pygame.image.load(Path("art/duck-1/duck_alpha_1_up.png"))
dimg_down = pygame.image.load(Path("art/duck-1/duck_alpha_1_down.png"))

win = pygame.display.set_mode((1920, 1080))
# win = pygame.display.set_mode((0, 0), pygame.RESIZABLE) # pygame.FULLSCREEN

pygame.display.set_caption("Walk Simulator")


def select_image(direction):
    if direction == "standing": return dimg_right
    if direction == "left": return dimg_left
    if direction == "right": return dimg_right
    if direction == "up": return dimg_up
    if direction == "down": return dimg_down
    


def redraw_view(duck: Duck):
    win.fill((10, 20, 30))
    if duck.location == "house": win.blit(house, (0, 0))
    if duck.location == "home": win.blit(home, (0, 0))
    
    win.blit(select_image(duck.get_direction()), (duck.x,duck.y))
    # pygame.draw.rect(win, (100, 150, 100), (duck.x, duck.y, duck.width, duck.height)) -- > pygame rectangle, colors with rgb and positioning
    pygame.display.update()