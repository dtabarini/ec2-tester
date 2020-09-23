from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import json
import pymongo
import ssl

app = Flask(__name__)
socketio = SocketIO(app)

db_string = "mongodb+srv://dtabarini:8tbFDUeD75u&e@test-cluster.yq5xx.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(db_string, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client.test


mydb = client["data"]
mycol = mydb["test"]

clients = []


@app.route("/")
def hello_world():

    x = mycol.insert_one({
        'ah': 'choo'
    })
    print(x)
    return "workded"


@app.route("/test-broadcast")
def test_broadcast():
    print("hello there", clients)
    socketio.emit("test_broadcast", room=clients[0])
    return "Did it work?"


@socketio.on("connect")
def test_connect():
    clients.append(request.sid)
    print("Client connected")


@socketio.on("disconnect")
def test_disconnect():
    clients.remove(request.sid)
    print("Client disconnected")


if __name__ == "__main__":
    socketio.run(app)
