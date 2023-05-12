#!/usr/bin/env python3

import pygame as pg
import sys
from random import randint
import math

from bubbles import Bubbles


colors: tuple = ("red", "green", "blue", "yellow", "purple", "orange")
delay: int = 100


def main():
    pg.init()
    pg.display.set_caption("Bubble shooter")
    screen = pg.display.set_mode((600, 480))
    clock = pg.time.Clock()
    bubbles = Bubbles(screen, colors)
    current_color = colors[randint(0, len(colors) - 1)]
    dt: float = 0
    time_elapsed: float = delay
    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

        bubbles.update()

        if time_elapsed >= delay:
            if pg.mouse.get_pressed()[0]:
                time_elapsed = 0
                current_color = colors[randint(0, len(colors) - 1)]
        else:
            time_elapsed += dt
            print(time_elapsed)

        screen.fill((30, 30, 30))
        bubbles.draw(screen)

        dist = 100
        p1 = (screen.get_width() / 2, screen.get_height())
        p2 = pg.mouse.get_pos()
        angle = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
        delta = (math.cos(angle) * dist, math.sin(angle) * dist)
        pg.draw.line(screen, (62, 63, 75), p1, (p1[0] + delta[0], p1[1] + delta[1]), 10)
        pg.draw.circle(screen, (52, 53, 65), p1, 25)
        pg.draw.circle(screen, current_color, p1, 15)

        pg.display.flip()
        dt = clock.tick(60)

    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()
