import pygame

class bullet():
    def __init__(self):
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()