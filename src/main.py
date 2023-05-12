#!/usr/bin/env python3

import pygame as pg
import sys

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
        bubbles.draw_rect(screen)
        pg.display.flip()
        clock.tick(60) / 1000

    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()
