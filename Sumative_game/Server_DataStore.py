#Import any dependncies
import pygame

# This class will act as a data storage for our server
class Sever_DS():
    #any and all class varibles




    #The method all on when the object is first made
    def __init__(self):
        self.projectiles = []
        self.players = []



        self.listofIDs = []

        pass


    #any and all class methods

    def UpdatePlayerInfo(self,id,pos,angle,rx,ry,rw,rh):
        for player in self.players:
            if player.id == id:
                player.Pos = pos
                player.angle = angle
                player.rect = pygame.Rect(rx,ry,rw,rh)


    def RemovePlayer(self,id):
        for player in self.players:
            if player.id == id:
                self.players.remove(player)


    def RemoveProjectile(self,id):
        for projectiles in self.projectiles:
            if projectiles.id == id:
                self.projectiles.remove(projectiles)


    def updateprojectile(self,id ):

        for projectle in self.projectiles:
            if projectle.id == id:
                projectle.update_pos()

    def updatehealth(self,id):
        for player in self.players:
            if player.id == id:
                return player.health