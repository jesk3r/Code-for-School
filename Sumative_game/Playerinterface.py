from flask import Flask,jsonify,request

app = Flask(__name__)

class character():

    def __init__(self):
        self.info = None
        self.id = None


player_ingame = []
player_ids = {}

@app.route('/giveInfo', methods=['POST'])
def setpos():
    values = request.get_json()

    #nt.info = values

    return jsonify("pos updated"),200


@app.route('/getInfo', methods=['GET'])
def sendpos():
    values = character.info

    return jsonify(values),200


@app.route('/handshake', methods=['POST'])
def handshake():
    values = request.get_json()

    #if values[id] not in player_ingame:
        #respond  = "lobby full"
        #return respond,200

    player = character()
    player.info = values['info']
    player.id = values['id']
    player_ids.update({values['id']: player})
    player_ingame.append(player)
    respond = "info recived entering game "
    return respond,200

@app.route('/getplayerinfo', methods=['GET','POST'])
def getplayerinfo():
    if request.method == 'POST':
        values = request.get_json()
        player = player_ids[values['id']]

        respond = {
            'angle': player.info['info']['angle'],
            'pos': player.info['info']['pos']
        }
        return respond
    else:
        frespond = []

        for player in player_ingame:
            respond = {player.id: {
                                'angle': player.info['angle'],
                                'pos': player.info['pos']

                                  }
                       }
            frespond.append(respond)

        return jsonify(frespond)

app.run(host='192.168.0.14',port=5000)