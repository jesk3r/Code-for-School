from flask import Flask,jsonify,request

app = Flask(__name__)

class character():
    n = 1
    nb = 0
    def __init__(self):
        self.info = None
        self.id = None
        self.name = None

player_ingame = []
player_ids = {}
player_names = {}
bullets = []

@app.route('/getplayersingame', methods=['GET'])
def setpos():
    values = player_ingame
    print(player_ids)
    respond = []
    for player in values:
        respond.append(player.__dict__)


    return jsonify(respond)



@app.route('/getInfo', methods=['GET'])
def sendpos():
    values = character.info

    return jsonify(values),200


@app.route('/handshake', methods=['POST'])
def handshake():
    values = request.get_json()

    print(values)
    if len(player_ingame) >= 6:
        respond  = "lobby full"
        return respond,200


    player = character()
    player.info = values['info']
    player.id = character.n
    #player.id = values['id' ]
    character.n += 1
    #player_ids.update({values['id']: player})
    player_ids.update({str(player.id): player})
    player_names.update({str(values['name']): player})
    player.name = values['name']
    player_ingame.append(player)
    respond = "info recived entering game "
    return respond,200

@app.route('/getplayerinfo', methods=['GET','POST'])
def getplayerinfo():
    if request.method == 'POST':
        values = request.get_json()

        player = player_names[str(values['name'])]

        respond = {
            "angle": player.info['angle'],
            "pos": player.info['pos']
            #"name": player.name
        }


        return jsonify(respond)
    else:
        frespond = []

        for player in player_ingame:

            respond = {player.id: {
                                'angle': player.info['angle'],
                                'pos': player.info['pos'],
                                'name': player.name
                                  }
                       }
            frespond.append(respond)

        return jsonify(frespond)






@app.route('/updateinfo', methods=['POST'])
def updateplayerinfo():
    values = request.get_json()
    print(player_names)
    player = player_names[values['name']]

    player.info = values['info']

    return "updated playerinfo",200


@app.route('/removeplayer', methods=['POST'])
def remove_player():
    values = request.get_json()

    for player in player_ingame:
        if player.name == values["name"]:
            player_ingame.remove(player)
            character.n -= 1
            break


        print(player)

    return "removed player", 200

@app.route('/makebullet', methods=['POST'])
def makebullet():
    values = request.get_json()
    print(values)
    b_values = {
        "x": values["x"],
        "y": values["y"]
    }

    bullets.append(b_values)
    return "bullet added", 200


@app.route('/getbullets', methods=['GET'])
def getbullets():
    frepond = []

    for b in bullets:
        block = {character.nb:{
            'x': b['x'],
            'y': b['y']
            }
        }
        frepond.append(block)



    return jsonify(frepond), 200


app.run(host='127.0.0.1',port=5000)