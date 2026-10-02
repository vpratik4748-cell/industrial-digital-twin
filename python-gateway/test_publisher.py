import paho.mqtt.client as mqtt
import json

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "industrial/pump/01/telemetry"

telemetry = {
    "flow": 74.3,
    "pressure": 4.12,
    "temperature": 53.8,
    "current": 7.9,
    "tank_level": 68.4,
    "status": "RUNNING"
}

payload = json.dumps(telemetry)

print("Sending:")
print(payload)

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

client.publish(TOPIC, payload)

client.disconnect()

print("Telemetry published successfully.")