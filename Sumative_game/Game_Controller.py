#import dependencies
import pygame
import math


class GC():
    '''''
    This class is used as a way to store bits of data need for the render engine 
    and as this class has methods that are going to be used in rendering, calculation for input
    among other useful things
    '''''
    #class vars
    DISPLAY_W = 800
    DISPLAY_L = 640


    # The method first called when the
    def __init__(self):
        self.Dx = 0
        self.Dy = 0

        self.ProjectileInPlay = []

        self.EnemyPlayers = []

        self.DeathBox = pygame.Rect(0,0,800,640)

        self.handshakedone = False

    #Other methods

    def get_angle(self,x1,y1,x2,y2):
        dx = x1 - x2
        dy = y1 - y2

        angle = math.atan2(dy,dx)

        angle = math.degrees(angle) - 90
        return  angle



    def rotate(self,surface, angle, pivot, offset = pygame.math.Vector2(0,2)):
        """Rotate the surface around the pivot point.
        Args:
            surface (pygame.Surface): The surface that is to be rotated.
            angle (float): Rotate by this angle.
            pivot (tuple, list, pygame.math.Vector2): The pivot point.
            offset (pygame.math.Vector2): This vector is added to the pivot.
        """
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect = rotated_image.get_rect(center=pivot + rotated_offset)
        return rotated_image, rect  # Return the rotated image and shifted rect.


    def alive(self,client):

        for projectiles in self.ProjectileInPlay:
            if not self.DeathBox.collidepoint(projectiles.pos[0],projectiles.pos[1]):

                self.ProjectileInPlay.remove(projectiles)
                client.RemoveBulllet(projectiles.id)


    def updateprojectile(self):
        pass
