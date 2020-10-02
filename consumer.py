import socketio
import sys


def ws_connect():
    print("Connected!")


def ws_disconnect():
    print("Disconnected!")


def test_broadcast():
    print("SUCCESS")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        environment_name = sys.argv[1]
        path = (
            "ws://" + environment_name + ".eba-e3eabptp.us-east-2.elasticbeanstalk.com"
        )
        path = "ws://fast-shore-55478.herokuapp.com/"

    else:
        path = "ws://localhost:5000"

    sio = socketio.Client()

    sio.on("connect", ws_connect)
    sio.on("disconnect", ws_disconnect)
    sio.on("test_broadcast", test_broadcast)

    sio.connect(path)
