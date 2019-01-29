#import any depenpendenies
import pygame
import math
import uuid
import os

class projectile():
    #class variables

    projectileImage = pygame.image.load( os.path.dirname(os.path.abspath(__file__)) + "/projectileh.png")
    speedvector = 10

    #first method that is called
    def __init__(self,pos):
        self.Velosty = None
        self.pos = pos
        self.Rimage = None
        self.rect = None
        self.angle = None
        self.id = str(uuid.uuid4())

    def Calculate_vector(self,angle):
        '''
        :argument:

            angle: an float number representing the angle from the normal
        '''

        Dx = self.speedvector * math.cos(math.radians(angle))
        Dy = self.speedvector * math.sin(math.radians(angle))

        self.Velosty = pygame.math.Vector2(Dx,Dy)

    def update_pos(self):
        '''
        updates the posion of our projectile acording to velosity vector

        '''

        self.pos += self.Velosty