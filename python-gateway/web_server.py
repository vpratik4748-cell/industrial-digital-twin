import json
import time
import threading

import paho.mqtt.client as mqtt

from flask import Flask, send_from_directory
from flask_sock import Sock


# ============================================================
# CONFIGURATION
# ============================================================

BROKER = "127.0.0.1"
PORT = 1883

TOPIC = "industrial/pump/01/telemetry"


# ============================================================
# LATEST TELEMETRY
# ============================================================

latest_data = {
    "flow": 0,
    "pressure": 0,
    "temperature": 0,
    "current": 0,
    "tank_level": 0,
    "status": "UNKNOWN"
}


# ============================================================
# MQTT CALLBACKS
# ============================================================

def on_connect(client, userdata, flags, rc):

    print("WebSocket server connected to MQTT!")

    client.subscribe(TOPIC)

    print(f"Subscribed to: {TOPIC}")


def on_message(client, userdata, msg):

    global latest_data

    try:

        payload = msg.payload.decode("utf-8")

        latest_data = json.loads(payload)

        print("Live telemetry updated:")
        print(latest_data)

    except json.JSONDecodeError:

        print("Invalid JSON received from MQTT")


# ============================================================
# MQTT CLIENT
# ============================================================

mqtt_client = mqtt.Client()

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(BROKER, PORT, 60)

# Start MQTT communication in background
mqtt_client.loop_start()


# ============================================================
# FLASK WEB SERVER
# ============================================================

app = Flask(__name__)

sock = Sock(app)


# ============================================================
# SERVE THREE.JS FRONTEND
# ============================================================

@app.route("/")
def index():

    return send_from_directory(
        "../frontend",
        "index.html"
    )


# ============================================================
# WEBSOCKET CONNECTION
# ============================================================

@sock.route("/ws")
def websocket(ws):

    print("Three.js browser connected!")

    while True:

        # Convert Python dictionary to JSON
        message = json.dumps(latest_data)

        # Send telemetry to browser
        ws.send(message)

        # Send once every second
        time.sleep(1)


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print()
    print("======================================")
    print(" INDUSTRIAL DIGITAL TWIN WEB SERVER")
    print("======================================")
    print("Dashboard: http://127.0.0.1:5000")
    print("WebSocket: ws://127.0.0.1:5000/ws")
    print()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )