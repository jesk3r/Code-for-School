# !/usr/bin/env python
import Bullet
import pygame
from pygame.locals import *
from sys import exit
import PlayermodelC as player
import math



bullet = Bullet.bullet()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Pygame Demo")

player = pygame.image.load("bullet.png").convert_alpha()


clock = pygame.time.Clock()
player_pos = pygame.math.Vector2(300, 350)
player_speed = 100.
v = pygame.math.Vector2(0., 0.)
bullet_velosity = 3
angle = 0
pivot = [200, 250]

def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
    rise = y1 - y2
    run = x1 - x2
    angle = math.atan2(run, rise) # get the angle in radians
    angle = angle * (180 / math.pi) # convert to degrees
    angle = (angle + 90) % 340 # adjust for a right-facing sprite
    return angle

def getDirection(angle,velostiy = bullet_velosity):
    x_value = velostiy * math.cos(math.radians(angle))
    y_value = velostiy * math.sin(math.radians(angle))
    #print(math.sin(math.radians(55)))

    return x_value,y_value

def rotate(surface, angle, pivot, offset):
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
    rect = rotated_image.get_rect(center=pivot+rotated_offset)
    return rotated_image, rect  # Return the rotated image and shifted rect.

bullets = pygame.sprite.Group()
while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            exit()

        if event.type == MOUSEBUTTONDOWN:
            bullet = Bullet.bullet()
            angle = getAngle(x1=player_pos[0], x2=event.pos[0], y1=player_pos[1], y2=event.pos[1])
            x,y = getDirection(angle)#gets the x and y slope
            v = pygame.math.Vector2(x-.25,-1*y)
            bullet.velostiy = pygame.math.Vector2(x-.25,-1*y)
            bullet.rotatedimage, rect = rotate(surface=player, angle=- angle + 90, pivot=v, offset=pygame.math.Vector2(0, -5))
            print(angle)
            bullets.add(bullet)
            print(bullets)


        if event.type == KEYUP:
            v = pygame.math.Vector2(0,0)

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_UP]:
        v = pygame.math.Vector2(-0.38181, -3.98174)
    elif pressed_keys[K_DOWN]:
        v = pygame.math.Vector2(0., 1.)
    elif pressed_keys[K_LEFT]:
        v = pygame.math.Vector2(-1., 0.)
    elif pressed_keys[K_RIGHT]:
        v = pygame.math.Vector2(1., 0.)
    else:
        #v = pygame.math.Vector2(0,0)
        pass

    pos = pygame.mouse.get_pos()
    screen.fill((255, 255, 255))

    player_draw_pos = pygame.math.Vector2(player_pos.x, player_pos.y)

    for b in bullets:
        bullets.draw(screen)
        b.update()
        #print(b.__dict__)
        print(b.rect)


    #rotated_image, rect = rotate(surface=player, angle = angle + 10, pivot=player_pos, offset=pygame.math.Vector2(0, 0))

    #screen.blit(rotated_image, rect)


    pos = pygame.mouse.get_pos()






    time_passed = clock.tick()

    time_passed_seconds = time_passed / 1000.0

    player_pos += bullet.velostiy * player_speed * time_passed_seconds

    pygame.display.update()