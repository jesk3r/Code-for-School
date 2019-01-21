import pygame

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([25,25])
        self.image.fill((255,0,0))
        self.rect = None
        self.velostiy = pygame.math.Vector2(0.0,0.0)
        self.speed = 3
        self.player_speed = 100
        self.vx = None
        self.vy = None


    def update(self):
        self.rect.x += self.vx * 5
        self.rect.y += self.vy * 5
