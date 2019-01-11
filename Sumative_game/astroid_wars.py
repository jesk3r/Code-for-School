import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys
import socket
import requests
from flask import jsonify
import PlayermodelC as player

Display_W = 800
Display_L = 640

DisplayScreen = pg.display.set_mode((Display_W,Display_L))
clock = pg.time.Clock()

pg.init()

Player = player.Playermodel()
class mouse_circle(pg.sprite.Sprite):

    def __init__(self,dp):
        super().__init__()

        self.pos = (0,0)

        self.cursor = pg.draw.circle(dp,((0,0,0)),self.pos,0)



def menu_animation():

    pg.mouse.set_visible(False)
    n = 1
    while n != 24:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                QUIT()

        frame = pg.image.load("/Users/dheeraj/Documents/git_projects/School_work/Coding_class/Sumative_game/Main Menu/Main Menu-{0} (dragged).png".format(n))

        DisplayScreen.blit(frame, ((0, 0)))

        clock.tick(24)
        pg.display.update()
        n += 1



def menu_screen():
    pg.mouse.set_visible(True)
    startA = pg.Rect((22, 246), (130, 40))
    quitA = pg.Rect((22, 300), (90, 40))

    frame = pg.image.load("/Users/dheeraj/Documents/git_projects/School_work/Coding_class/Sumative_game/Main Menu/Main Menu-23 (dragged).png").convert()

    while True:
        pos = pg.mouse.get_pos()
        mclicks = pg.mouse.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                QUIT()

        if startA.collidepoint(pos) and mclicks[0] == 1:
            gameloop()

        elif quitA.collidepoint(pos) and mclicks[0] == 1:
            sys.exit()

        DisplayScreen.blit(frame, ((0, 0)))

        clock.tick(24)
        pg.display.update()


def rotate(surface, angle, pivot, offset):
    """Rotate the surface around the pivot point.

    Args:
        surface (pygame.Surface): The surface that is to be rotated.
        angle (float): Rotate by this angle.
        pivot (tuple, list, pygame.math.Vector2): The pivot point.
        offset (pygame.math.Vector2): This vector is added to the pivot.
    """
    rotated_image = pg.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
    rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
    # Add the offset vector to the center/pivot point to shift the rect.
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.



def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
    rise = y1 - y2
    run = x1 - x2
    angle = math.atan2(run, rise) # get the angle in radians
    angle = angle * (180 / math.pi) # convert to degrees
    angle = (angle + 90) % 340 # adjust for a right-facing sprite
    return angle


#game loop function
def gameloop():
    pg.mouse.set_visible(True)



    DisplayScreen.fill((0, 0, 0))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.mouse.set_visible(True)
                running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            Player.pivot[0] += 10
        elif keys[pg.K_a] or keys[pg.K_LEFT]:
            Player.pivot[0] -= 10
        if keys[pg.K_w]:
            Player.pivot[1] -= 10
        if keys[pg.K_s]:
            Player.pivot[1] += 10

        DisplayScreen.fill((0,0,0))

        mos = pg.mouse.get_pos()


        Player.angle = getAngle(Player.pivot[0], Player.pivot[1], mos[0], mos[1])



        try:
            r = requests.post("http://192.168.0.14:5000/giveInfo",json = {'pos':Player.pivot,'angle': Player.angle,})
            #r = requests.get("http://0.0.0.0:5000/ge")
            print(r.json())
        except:
            pass


        # Rotated version of the image and the shifted rect.
        rotated_image, rect = rotate(surface=Player.image, angle =- Player.angle + 90, pivot=Player.pivot, offset=Player.offset)

        DisplayScreen.blit(rotated_image, rect)

        clock.tick(60)
        pg.display.update()


if __name__ == "__main__":
    gameloop()

