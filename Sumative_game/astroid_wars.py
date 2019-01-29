#!/usr/bin/env python

# Import file dependices
import pygame as pg
import User_Interface as UI
import Player
import Projectile
import Game_Controller
import Client
import atexit

#init The screen
DisplayScreen = pg.display.set_mode((Game_Controller.GC.DISPLAY_W,Game_Controller.GC.DISPLAY_L))

#init Variables
playerUI = UI.UserInterface()

player = Player.player()

client = Client.client(player)

#pre game set up #1

player.setid()
client.EnemiesId.append(player.id)

gamecontroller = Game_Controller.GC()


#The Main game loop(This is where the things will be displayed on screen)
def gameloop():
    while True:
        #requtes data from UI
        event = playerUI.Event_Handler()

        #uses the data form the Event Handler to affect the player in the game
        if event[0] != 0:
            # just do nothing
            pass
        if event[0] == 1:
            #create a projectile

            #makes sure that the player can only make 3 bullets
            if len(gamecontroller.ProjectileInPlay) <= 3:
                projectile = Projectile.projectile(pos = [player.Pos[0] ,player.Pos[1] -50 ] )


                projectile.angle = player.angle - 90

                projectile.Calculate_vector(projectile.angle)

                projectile.Rimage,projectile.rect = gamecontroller.rotate(surface = projectile.projectileImage ,angle = player.angle ,pivot = projectile.pos  ,)

                gamecontroller.ProjectileInPlay.append(projectile)



                client.SpawnBullet(gamecontroller,projectile)

                client.MyProjectiles.append(projectile.id)

        #start del

        if event[0] == 2:

            #the value of the key
            if event[1] == pg.K_d:


                gamecontroller.Dx = 7

            elif event[1] == pg.K_a:


                gamecontroller.Dx = -7

            elif event[1] == pg.K_w:


                gamecontroller.Dy = -7

            elif event[1] == pg.K_s:


                gamecontroller.Dy = 7


        if event[0] == 3:
            #Nothing really just stop the player from moving

            if event[1] == pg.K_d :
                gamecontroller.Dx = 0

            if event[1] == pg.K_s :
                gamecontroller.Dy = 0

            if event[1] == pg.K_w:
                gamecontroller.Dy = 0

            if event[1] == pg.K_a:
                gamecontroller.Dx = 0

        #end of del


        #compulations to update player
        mpos = pg.mouse.get_pos()
        player.update_angle(gamecontroller.get_angle(x1=player.Pos[0], y1=player.Pos[1], x2=mpos[0], y2=mpos[1]))



        #update our player info
        player.update_pos([player.Pos[0] + gamecontroller.Dx, player.Pos[1] + gamecontroller.Dy])

        player.Rmodel,player.rect = gamecontroller.rotate(surface = player.player_model,angle = player.angle ,pivot = player.Pos)

        #transmit our data to the server

        if gamecontroller.handshakedone == False:
            client.Handshake()
            gamecontroller.handshakedone = True

        client.UpdatePlayerInfo()


        #update projecitle
        for projectile in gamecontroller.ProjectileInPlay:
            projectile.update_pos()


        # update player info on the screen
        DisplayScreen.fill((0,0,0))
        DisplayScreen.blit(player.Rmodel, player.rect)

        #draws every projectile
        client.GetProjectiles()

        for projectile in gamecontroller.ProjectileInPlay:

            DisplayScreen.blit(projectile.Rimage,projectile.pos)


            client.projectileidlist.append(projectile.id)



        for projectile in client.ProjectilesInGame:
            DisplayScreen.blit(projectile.Rimage,projectile.pos)

        #update projectile data on the server
        client.updateprojectiles(gamecontroller)

        #clear data
        client.ProjectilesInGame.clear()
        client.projectileidlist.clear()

        gamecontroller.alive(client)

        client.hitbox()

        #update our health
        client.getheath(player)

        print(player.health)

        #ask for data from the client
        client.GetPlayersIngame()


        # Render client data

        #first render the players
        for enemy in client.EnemiesInGame:
            enemy.Rmodel,enemy.rect = gamecontroller.rotate(surface= Player.player.enemy_modle, angle = enemy.angle , pivot = enemy.Pos)
            DisplayScreen.blit(enemy.Rmodel,enemy.rect)

        client.EnemiesInGame.clear()

        #Then render the bullets


        pg.display.update()


atexit.register(client.ExitGame)


if __name__ == "__main__":
    gameloop()

