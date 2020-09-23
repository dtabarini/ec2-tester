from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return "hw"


@socketio.on('send_message')
def handle_source(json_data):
    text = json_data['message'].encode('ascii', 'ignore')
    print('hello')
    socketio.emit('echo', {'echo': 'Server Says: '+text})


if __name__ == "__main__":
    socketio.run(app)
