import pygame as pg


import settings
import platforms
import time 

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -4300

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pg.sprite.Group()
        self.enemy_list = pg.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(settings.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1 """

    def __init__(self, player):
        """ Create level 1 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pg.image.load("background_01.png").convert()
        self.background.set_colorkey(settings.WHITE)
        self.level_limit = -4300

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 570, 500],
                  [platforms.GRASS_RIGHT, 640, 500],
                  
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  
                  [platforms.GRASS_LEFT, 1760, 280],
                  [platforms.GRASS_MIDDLE, 1830, 280],
                  [platforms.GRASS_RIGHT, 1900, 280],
                  
                  [platforms.STONE_PLATFORM_LEFT, 2050, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 2120, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 2190, 400],
                  
                  [platforms.GRASS_LEFT, 2790, 180],
                  [platforms.GRASS_MIDDLE, 2860, 180],
                  [platforms.GRASS_RIGHT, 2930, 180],
                  
                  [platforms.GRASS_LEFT, 3640, 220],
                  [platforms.GRASS_MIDDLE, 3710, 220],
                  [platforms.GRASS_RIGHT, 3780, 220],

                  [platforms.STONE_PLATFORM_LEFT, 4050, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 4120, 150],
                  [platforms.STONE_PLATFORM_RIGHT, 4190, 150],

                  [platforms.GRASS_LEFT, 4490, 280],
                  [platforms.GRASS_MIDDLE, 4560, 280],
                  [platforms.GRASS_RIGHT, 4630, 280]
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1670
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2500
        block.rect.y = 300
        block.boundary_left = 2300
        block.boundary_right = 2700
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 3090
        block.rect.y = 200
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 3500
        block.rect.y = 350
        block.boundary_left = 3200
        block.boundary_right = 3550
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 4800
        block.rect.y = 400
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 5100
        block.rect.y = 400
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2 """

    def __init__(self, player):
        """ Create level 2 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pg.image.load("background_01.png").convert()
        self.background.set_colorkey(settings.WHITE)
        self.level_limit = -4000

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 350, 475],
                  [platforms.STONE_PLATFORM_MIDDLE, 420, 475],
                  [platforms.STONE_PLATFORM_RIGHT, 490, 475],
                  
                  [platforms.GRASS_LEFT, 750, 350],
                  [platforms.GRASS_MIDDLE, 820, 350],
                  [platforms.GRASS_RIGHT, 890, 350],
                  
                  [platforms.STONE_PLATFORM_LEFT, 1200, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1270, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1340, 280],
                  
                  [platforms.STONE_PLATFORM_LEFT, 1740, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1810, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1880, 280],

                  [platforms.GRASS_LEFT, 2000, 140],
                  [platforms.GRASS_MIDDLE, 2070, 140],
                  [platforms.GRASS_RIGHT, 2140, 140],

                  [platforms.GRASS_LEFT, 2340, 300],
                  [platforms.GRASS_MIDDLE, 2410, 300],
                  [platforms.GRASS_RIGHT, 2480, 300],

                  [platforms.GRASS_LEFT, 2850, 250],
                  [platforms.GRASS_MIDDLE, 2920, 250],
                  [platforms.GRASS_RIGHT, 2990, 250],

                  [platforms.STONE_PLATFORM_LEFT, 3740, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 3810, 150],
                  [platforms.STONE_PLATFORM_RIGHT, 3880, 150],

                  [platforms.STONE_PLATFORM_LEFT, 4440, 350],
                  [platforms.STONE_PLATFORM_MIDDLE, 4510, 350],
                  [platforms.STONE_PLATFORM_RIGHT, 4580, 350],

                  [platforms.GRASS_LEFT, 4850, 280],
                  [platforms.GRASS_MIDDLE, 4920, 280],
                  [platforms.GRASS_RIGHT, 4990, 280]

                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1540
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 3300
        block.rect.y = 250
        block.boundary_left = 3100
        block.boundary_right = 3500
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 4100
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_03(Level):
    """ Definition for level 3 """

    def __init__(self, player):
        """ Create level 3 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pg.image.load("background_01.png").convert()
        self.background.set_colorkey(settings.WHITE)
        self.level_limit = -4300

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 250, 500],
                  [platforms.STONE_PLATFORM_MIDDLE, 320, 500],
                  [platforms.STONE_PLATFORM_RIGHT, 390, 500],
                  
                  [platforms.GRASS_LEFT, 750, 400],
                  [platforms.GRASS_MIDDLE, 820, 400],
                  [platforms.GRASS_RIGHT, 890, 400],

                  
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],

                  [platforms.GRASS_LEFT, 2000, 400],
                  [platforms.GRASS_MIDDLE, 2070, 400],
                  [platforms.GRASS_RIGHT, 2140, 400],

                  [platforms.STONE_PLATFORM_LEFT, 2420, 300],
                  [platforms.STONE_PLATFORM_MIDDLE, 2490, 300],
                  [platforms.STONE_PLATFORM_RIGHT, 2560, 300],

                  [platforms.STONE_PLATFORM_LEFT, 3140, 300],
                  [platforms.STONE_PLATFORM_MIDDLE, 3210, 300],
                  [platforms.STONE_PLATFORM_RIGHT, 3280, 300],

                  [platforms.GRASS_LEFT, 4100, 175],
                  [platforms.GRASS_MIDDLE, 4170, 175],
                  [platforms.GRASS_RIGHT, 4240, 175],

                  [platforms.GRASS_LEFT, 4500, 375],
                  [platforms.GRASS_MIDDLE, 4570, 375],
                  [platforms.GRASS_RIGHT, 4640, 375],

                  [platforms.GRASS_LEFT, 4870, 275],
                  [platforms.GRASS_MIDDLE, 4940, 275],
                  [platforms.GRASS_RIGHT, 5010, 275],
    
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1700
        block.rect.y = 280
        block.boundary_left = 1400
        block.boundary_right = 1750
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2840
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 3800
        block.rect.y = 490
        block.boundary_left = 3400
        block.boundary_right = 4200
        block.change_x = 5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 3800
        block.rect.y = 200
        block.boundary_top = 100
        block.boundary_bottom = 400
        block.change_y = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_04(Level):
    """ Definition for level 4 """

    def __init__(self, player):
        """ Create level 4 """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pg.image.load("background_01.png").convert()
        self.background.set_colorkey(settings.WHITE)
        self.level_limit = -600

        # Array with type of platform, and x, y location of the platform.
        level = []


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

