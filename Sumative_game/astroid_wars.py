import pygame as pg
import User_Interface as UI

#!/usr/bin/env python

player = UI.UserInterface()
#game loop function

DisplayScreen = pg.display.set_mode((800,600))


def gameloop():
    while True:

        player.Event_Handler()
        pg.display.update()

if __name__ == "__main__":
    gameloop()

