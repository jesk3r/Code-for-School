# Import dependices
from flask import Flask,jsonify,request
import Server_DataStore
import Player
import pygame
import Projectile

#Create The serverdata object
ServerData  = Server_DataStore.Sever_DS()


#Create flask server
app = Flask(__name__)

@app.route('/HandShake', methods= ['POST'])
def HandShake():
    values = request.get_json()

    respond = None

    if  len(ServerData.players) <= 5 :
        player = Player.player()

        player.angle = values['angle']
        player.id = values['id']
        player.rect = pygame.Rect(values['rx'],values['ry'],values['rw'],values['rh'])
        player.health = 1
        player.Pos = values['pos']

        ServerData.players.append(player)

        print(ServerData.players)

        respond = "Hand shake confirmed, now entering going online"

    else:
        respond = "server full"


    return respond,200


@app.route("/UpdatePlayerInfo", methods = ['POST'])
def UpdatePlayerInfo():
    values = request.get_json()

    ServerData.UpdatePlayerInfo(
        pos=values['pos'],
        id=values['id'],
        angle=values['angle'],
        rx=values['rx'],
        ry= values['ry'],
        rh= values['rh'],
        rw= values['rw']
    )

    return "Player Info update",200

@app.route("/GetPlayerInfo", methods = ['GET'])
def GetPlayerInfo():

    respond = []

    for player in ServerData.players:
        data =  {
                    'angle' : player.angle,
                    'pos': player.Pos,
                    'id': player.id,
                    'hp': player.health
                }
        respond.append(data)


    return jsonify(respond),200

@app.route("/RemovePlayer", methods = ['POST'])
def RemovePlayer():
    values = request.get_json()

    ServerData.RemovePlayer(values['id'])

    return "Player Removed", 200

@app.route("/SpawnBullet", methods = ['POST'])
def SpawnBullet():
    values = request.get_json()

    b_in  = True

    for p in ServerData.projectiles:
        if p.id == values["id"]:
            b_in = False

    if b_in == True:
        projectile = Projectile.projectile(pygame.math.Vector2(values["pos"][0],values["pos"][1]))

        projectile.id = values["id"]
        projectile.angle = values["angle"]
        projectile.Velosty = pygame.math.Vector2(values["Velosity"][0],values["Velosity"][1])

        ServerData.projectiles.append(projectile)

    return "bullet added",200

@app.route("/GetBullet", methods = ['GET'])
def GetBullet():
    respond = []

    for projectile in ServerData.projectiles:
        data = {
            'angle': projectile.angle,
            'pos': [projectile.pos.x,projectile.pos.y],
            'id': projectile.id
        }
        respond.append(data)


    return jsonify(respond),200

@app.route("/UpdateProjectile", methods = ['POST'])
def UpdateProjectile():
    values = request.get_json()

    ServerData.updateprojectile(values['id'])

    return "projectile pos updated", 200


@app.route("/RemoveBullet", methods = ['POST'])
def RemoveBullet():
    values = request.get_json()

    ServerData.RemoveProjectile(values['id'])

    return "Removed projectile",200


@app.route("/Hitbox", methods = ['GET'])
def Hitbox():

    for players in ServerData.players:
        for projectile in ServerData.projectiles:
            print(players.rect.collidepoint(projectile.pos))
            if players.rect.collidepoint(projectile.pos):
                print(players.health)
                players.health -= 1
                break



    return "hitboxed",200

@app.route("/gethealth", methods = ['POST'])
def gethealth():
    values = request.get_json()

    hp = ServerData.updatehealth(values['id'])

    respond = {"hp": hp}

    return jsonify(respond),200


app.run(host='127.0.0.1',port=5000,)


