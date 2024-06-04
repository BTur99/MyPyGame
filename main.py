import random

import pygame as pg

size = (500, 500)
screen = pg.display.set_mode(size)
while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    screen.fill(pg.Color(r, g, b))

    pg.display.flip()