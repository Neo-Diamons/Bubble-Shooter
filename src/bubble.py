import pygame as pg


class Bubble(pg.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.x: int = x
        self.y: int = y
        self.color = color
        self.radius: int = radius
        self.detect_radius: int = radius * 3
        self.rect = pg.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        self.as_collided: bool = False

    def is_collided(self, bubbles: list, collided=None):
        bubbles.remove(self)
        if collided is None:
            collided = []
        collided.append(self)
        for bubble in bubbles:
            if self.color == bubble.color \
                    and (bubble.x - self.x) ** 2 + (bubble.y - self.y) ** 2 <= self.detect_radius ** 2:
                bubble.is_collided(bubbles, collided)
        return collided

    def update(self, bubbles: list, max_collided: int):
        if self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            self.is_collided(bubbles.copy())
            if len(self.is_collided(bubbles.copy())) >= max_collided:
                for bubble in self.is_collided(bubbles.copy()):
                    bubbles.remove(bubble)

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def draw_rect(self, screen):
        surface = pg.Surface((self.radius * 2, self.radius * 2))
        surface.set_alpha(100)
        if self.as_collided:
            surface.fill((255, 0, 0))
        else:
            surface.fill((255, 255, 255))
        screen.blit(surface, (self.x - self.radius, self.y - self.radius))
