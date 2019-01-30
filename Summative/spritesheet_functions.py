import pygame as pg

import settings

class SpriteSheet(object):

    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name):

        # Load the sprite sheet.
        self.sprite_sheet = pg.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        # Create a new blank image
        image = pg.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(settings.BLACK)

        # Return the image
        return image
