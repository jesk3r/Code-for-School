from flask import Flask,jsonify,request

app = Flask(__name__)

class network():

    def __init__(self):
        self.info = None

nt = network()


@app.route('/giveInfo', methods=['POST'])
def setpos():
    values = request.get_json()

    nt.info = values

    return jsonify("pos updated"),200


@app.route('/getInfo', methods=['GET'])
def sendpos():
    values = nt.info

    return jsonify(values),200



app.run(host='192.168.0.14',port=5000)