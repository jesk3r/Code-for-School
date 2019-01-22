#!/usr/bin/env python
import pygame as pg
from uuid import uuid4


class Playermodel(pg.sprite.Sprite):
    pivot = [200, 250]
    offset = pg.math.Vector2(0, -5)
    angle = 0
    image = pg.image.load("spaceshipV3.png")
    name = "hello"

    def __init__(self):

        super().__init__()
        self.pivot = self.pivot
        self.offset = pg.math.Vector2(0, -5)
        self.angle = 0
        self.id = str(uuid4())

        self.image = pg.image.load("spaceshipV3.png")



