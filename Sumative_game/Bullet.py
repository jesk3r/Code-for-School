import pygame

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("bullet.png")
        self.rect = pygame.math.Vector2(50,20)
        self.rotatedimage = None
        self.velostiy = pygame.math.Vector2(0.0,0.0)
        self.speed = 3
        self.player_speed = 100
        self.time_passed = 82


    def update(self):



        time_passed_seconds = self.time_passed / 1000.0


        self.rect += self.velostiy * self.player_speed * time_passed_seconds
        print(self.velostiy * self.player_speed * time_passed_seconds)

