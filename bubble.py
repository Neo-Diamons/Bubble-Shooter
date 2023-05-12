import pygame as pg


class Bubble(pg.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.x: int = x
        self.y: int = y
        self.color = color
        self.radius: int = radius
        self.rect = pg.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self):
        return self.rect.collidepoint(pg.mouse.get_pos())

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def draw_rect(self, screen):
        pg.draw.rect(screen, "red", self.rect)
