from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import json

app = Flask(__name__)
socketio = SocketIO(app)


clients = []


@app.route("/")
def hello_world():
    return jsonify({"msg": len(clients)})


@app.route("/test-broadcast")
def test_broadcast():
    print("hello there")
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
