#!/usr/bin/env python3
import math

import pygame as pg
import sys

import pygame.draw

from bubbles import Bubbles


colors: tuple = ("red", "green", "blue", "yellow", "purple", "orange")


def main():
    pg.init()
    pg.display.set_caption("Bubble shooter")
    screen = pg.display.set_mode((600, 480))
    clock = pg.time.Clock()
    bubbles = Bubbles(screen, colors)
    run = True

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

        bubbles.update()

        screen.fill((30, 30, 30))
        bubbles.draw(screen)

        dist = 100
        p1 = (screen.get_width() / 2, screen.get_height())
        p2 = pg.mouse.get_pos()
        angle = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
        delta = (math.cos(angle) * dist, math.sin(angle) * dist)
        pg.draw.line(screen, (255, 0, 0), p1, (p1[0] + delta[0], p1[1] + delta[1]), 3)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()
