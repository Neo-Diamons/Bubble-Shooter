from math import floor
from random import randint

from bubble import Bubble


class Bubbles:
    def __init__(self, screen, colors):
        self.bubbles: list = []
        self.circle_color: tuple = (255, 255, 255)
        self.circle_radius: int = 15
        self.circle_padding: int = 3
        self.max_collided: int = 3

        self.init_circle(screen, colors)

    def init_circle(self, screen, colors):
        padding = self.circle_radius + self.circle_padding
        step = self.circle_radius * 2 + self.circle_padding

        for y in range(padding, floor((screen.get_height() - step) / 100 * 75), step):
            if (y - padding) % (step * 2):
                loop_range = range(screen.get_width() - step, padding, -step)
            else:
                loop_range = range(step, screen.get_width() - padding, step)
            for x in loop_range:
                list.append(self.bubbles, Bubble(x, y, self.circle_radius, colors[randint(0, len(colors) - 1)]))

    def update(self):
        for bubble in self.bubbles:
            bubble.update(self.bubbles, self.max_collided)

    def draw(self, screen):
        for bubble in self.bubbles:
            bubble.draw(screen)

    def draw_rect(self, screen):
        for bubble in self.bubbles:
            bubble.draw_rect(screen)
