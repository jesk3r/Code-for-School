#import depndencis
import pygame
from uuid import uuid4

class player():
    player_model = pygame.image.load("spaceshipV3.png")
    enemy_modle = pygame.image.load("spaceshipEV3.png")
    def __init__(self):
        self.Pos = [400,360]
        self.angle = 0
        self.health = None
        self.id = None
        self.rect = None
        self.Rmodel = None


    #methods for this class

    def update_pos(self,pos ):
        '''''
        Args:
             pos is list
        '''

        self.Pos = pos

        pass

    def update_angle(self,angle):
        '''
        :arg

        angle : is a float
        '''

        self.angle = angle


    def update_health(self):
        '''
        this removes 1 hp from the health pool
        '''

        self.health -= 1

    def setid(self):
        '''
        This just sets a random id for our player
        :return: None
        '''

        self.id = str(uuid4())