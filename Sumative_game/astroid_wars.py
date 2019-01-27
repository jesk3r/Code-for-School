#!/usr/bin/env python

# Import file dependices
import pygame as pg
import User_Interface as UI
import Player.player


#init Variables
player = UI.UserInterface()


#init The screen
DisplayScreen = pg.display.set_mode((800,600))

#The Main game loop(This is where the things will be displayed on screen)
def gameloop():
    while True:

        #requtes data from UI
        player.Event_Handler()



        #update our player info





        # update info on the screen

        pg.display.update()

if __name__ == "__main__":
    gameloop()

