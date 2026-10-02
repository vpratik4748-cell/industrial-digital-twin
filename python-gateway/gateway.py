import paho.mqtt.client as mqtt
import json
import sqlite3
import joblib
import numpy as np
from datetime import datetime


BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "industrial/pump/01/telemetry"

DB_FILE = "database/telemetry.db"
MODEL_FILE = "ml/pump_anomaly_model.pkl"


# Load trained ML model
model = joblib.load(MODEL_FILE)

print("✓ ML anomaly model loaded.")


def initialize_database():

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            flow REAL,
            pressure REAL,
            temperature REAL,
            current REAL,
            tank_level REAL,
            status TEXT,
            anomaly TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("✓ Database initialized.")


def analyze_pump(data):

    input_data = np.array([
        [
            data["flow"],
            data["pressure"],
            data["temperature"],
            data["current"],
            data["tank_level"]
        ]
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        return "NORMAL"

    return "ML ANOMALY"


def save_telemetry(data, anomaly):

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO telemetry
        (
            timestamp,
            flow,
            pressure,
            temperature,
            current,
            tank_level,
            status,
            anomaly
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        data["flow"],
        data["pressure"],
        data["temperature"],
        data["current"],
        data["tank_level"],
        data["status"],
        anomaly
    ))

    conn.commit()
    conn.close()


def on_connect(client, userdata, flags, rc):

    print("Connected to MQTT broker!")
    print(f"Listening to: {TOPIC}")

    client.subscribe(TOPIC)


def on_message(client, userdata, msg):

    print("\n--- MQTT MESSAGE RECEIVED ---")

    try:

        raw_payload = msg.payload.decode("utf-8")

        print(f"Raw payload: {raw_payload}")

        data = json.loads(raw_payload)

        anomaly = analyze_pump(data)

        print("\n--- PUMP TELEMETRY ---")

        print(f"Flow       : {data['flow']} L/min")
        print(f"Pressure   : {data['pressure']} bar")
        print(f"Temperature: {data['temperature']} °C")
        print(f"Current    : {data['current']} A")
        print(f"Tank Level : {data['tank_level']} %")
        print(f"Status     : {data['status']}")

        print(f"ML Analysis: {anomaly}")

        save_telemetry(data, anomaly)

        print("✓ Telemetry saved to database.")

    except json.JSONDecodeError:

        print("⚠️ INVALID JSON PAYLOAD")

    except KeyError as e:

        print(f"⚠️ MISSING TELEMETRY FIELD: {e}")

    except Exception as e:

        print(f"⚠️ UNEXPECTED ERROR: {e}")


initialize_database()


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message


print("Starting Industrial IoT Gateway...")


client.connect(
    BROKER,
    PORT,
    60
)


client.loop_forever()