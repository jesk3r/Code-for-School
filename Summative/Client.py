#Import dependencies
import requests
import Player
import Projectile
import Game_Controller
import sys

#set up any varibles
gamecontroller = Game_Controller.GC()

#Creating a Client class
class client():
    #class variables


    #the first method called when the class is made
    def __init__(self,player):
        self.player = player

        self.EnemiesInGame = [] #An list of obj
        self.ProjectilesInGame = []

        self.projectileidlist =[]

        self.EnemiesId = [0]

        self.MyProjectiles = []

    #methods of client

    def Handshake(self):

        #This is the Json data send first during the hand shake
        Jdata = {
            "pos": self.player.Pos,
            "id": self.player.id,
            "angle": self.player.angle,
            "rx": self.player.rect.x,
            "ry": self.player.rect.y,
            "rh": self.player.rect.h,
            "rw": self.player.rect.w
        }

        requests.post("http://127.0.0.1:5000/HandShake", json= Jdata)

    def ExitGame(self):
        #Exit the game online

        for b in self.MyProjectiles:
            self.RemoveBulllet(b)

        Jdata = {
            "id": self.player.id
        }

        requests.post("http://127.0.0.1:5000/RemovePlayer", json = Jdata)

    def UpdatePlayerInfo(self):
        #Update player info
        Jdata = {
            "pos": self.player.Pos,
            "id": self.player.id,
            "angle": self.player.angle,
            "rx": self.player.rect.x,
            "ry": self.player.rect.y,
            "rh": self.player.rect.h,
            "rw": self.player.rect.w
        }

        requests.post("http://127.0.0.1:5000/UpdatePlayerInfo", json = Jdata)

    def GetPlayersIngame(self):
        data = requests.get("http://127.0.0.1:5000/GetPlayerInfo")
        values = data.json()
        Enemy = Player.player()

        for i in values:
            if i['id']  != self.player.id:
                Enemy = Player.player()

                Enemy.angle = i['angle']
                Enemy.Pos = i['pos']

                self.EnemiesInGame.append(Enemy)

    def GetProjectiles(self):
        data = requests.get("http://127.0.0.1:5000/GetBullet")
        values = data.json()

        for i in values:

            if i['id'] in self.projectileidlist:
                print("in this ")

            if i["id"] not in self.MyProjectiles:
                projectils = Projectile.projectile(pos=([i['pos'][0], i['pos'][1]]))
                projectils.angle = i['angle']

                projectils.Rimage ,projectils.rect = gamecontroller.rotate(surface = Projectile.projectile.projectileImage ,angle = projectils.angle ,pivot = projectils.pos ,)

                self.ProjectilesInGame.append(projectils)
                self.projectileidlist.append(i['id'])






    def SpawnBullet(self,gc,projectiles):

            Jdata = {
                "id": projectiles.id,
                "pos": projectiles.pos,
                "angle": self.player.angle,
                "Velosity": [projectiles.Velosty.x, projectiles.Velosty.y]
            }

            requests.post("http://127.0.0.1:5000/SpawnBullet", json =Jdata)




    def RemoveBulllet(self,id):

        Jdata = {
            "id": id
        }

        requests.post("http://127.0.0.1:5000/RemoveBullet", json= Jdata)


    def updateprojectiles(self,gc):
        for projectiles in gc.ProjectileInPlay:

            Jdata = {
                "id": projectiles.id
            }

            requests.post("http://127.0.0.1:5000/UpdateProjectile", json = Jdata)


    def getheath(self,player):

        Jdata = {
            "id": player.id
        }

        data = requests.post("http://127.0.0.1:5000/gethealth", json = Jdata)

        values = data.json()

        print(values)
        if values['hp'] < 0:
            sys.exit()



    def hitbox(self):
        requests.get("http://127.0.0.1:5000/Hitbox")
