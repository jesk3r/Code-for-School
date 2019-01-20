import pygame

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25,25])
        self.image.fill((255,200,0))
        self.rect = self.image.get_rect()
        self.clock = 60

    def update(self,vector,speed):
        """ updates each block making it move in a direction with a cuirtin speed

        :arg
            speed - How fast the block moves in a direction
            vector - in what direction the block moves

        :return: None
        """



        time_passed_seconds = self.clock/ 1000.0

        self.rect += vector * speed * time_passed_seconds
