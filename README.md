\# Industrial Digital Twin and IIoT Monitoring System



A simulated industrial pump-station Digital Twin integrating MQTT-based IIoT telemetry, Python data processing, machine-learning anomaly detection, SQLite data logging, WebSockets, and a Three.js 3D HMI.



\## Project Overview



This project simulates a Pump-01 industrial process and connects sensor telemetry to a software-based Digital Twin.



The current prototype demonstrates:



\* MQTT telemetry communication

\* JSON-based industrial telemetry

\* Python IIoT gateway

\* SQLite telemetry historian

\* Machine-learning anomaly detection

\* WebSocket communication

\* Three.js 3D Digital Twin

\* Browser-based HMI

\* Simulated normal and abnormal pump conditions



Additional industrial automation components such as ESP32/FreeRTOS, TinyML, PLC/Modbus, OPC UA, SCADA integration, OT cybersecurity, Docker and Linux deployment are planned for subsequent stages.



\## System Architecture



```text

&#x20;                        ┌──────────────────────┐

&#x20;                        │   THREE.JS DIGITAL   │

&#x20;                        │        TWIN          │

&#x20;                        │                      │

&#x20;                        │ Pump • Tank • HMI    │

&#x20;                        └──────────▲───────────┘

&#x20;                                   │

&#x20;                                WebSocket

&#x20;                                   │

&#x20;                        ┌──────────┴───────────┐

&#x20;                        │    PYTHON GATEWAY    │

&#x20;                        │                      │

&#x20;                        │ MQTT • ML • SQLite   │

&#x20;                        └──────────▲───────────┘

&#x20;                                   │

&#x20;                                  MQTT

&#x20;                                   │

&#x20;                        ┌──────────┴───────────┐

&#x20;                        │    MOSQUITTO MQTT    │

&#x20;                        │       BROKER         │

&#x20;                        └──────────▲───────────┘

&#x20;                                   │

&#x20;                        ┌──────────┴───────────┐

&#x20;                        │ Pump Telemetry       │

&#x20;                        │ Normal / Failure     │

&#x20;                        └──────────────────────┘

```



\## Current Data Flow



```text

Pump telemetry

&#x20;     ↓

MQTT

&#x20;     ↓

Mosquitto broker

&#x20;     ↓

Python gateway

&#x20;     ↓

Machine-learning inference

&#x20;     ↓

SQLite historian

&#x20;     ↓

WebSocket

&#x20;     ↓

Three.js Digital Twin / HMI

```



\## Telemetry



Pump-01 currently publishes:



| Parameter   | Unit  |

| ----------- | ----- |

| Flow        | L/min |

| Pressure    | bar   |

| Temperature | °C    |

| Current     | A     |

| Tank Level  | %     |

| Status      | State |



Telemetry is transmitted as JSON over MQTT.



Example:



```json

{

&#x20; "flow": 74.3,

&#x20; "pressure": 4.12,

&#x20; "temperature": 53.8,

&#x20; "current": 7.9,

&#x20; "tank\_level": 68.4,

&#x20; "status": "RUNNING"

}

```



\## Machine Learning



A Decision Tree classifier is currently used for pump anomaly detection.



The prototype training dataset contains simulated normal and anomalous operating conditions.



The current test run achieved approximately:



\*\*99.5% test accuracy\*\*



This result is based on synthetic training/test data and should not be interpreted as real-world pump-failure prediction accuracy.



The trained model is stored in:



```text

ml/pump\_anomaly\_model.pkl

```



\## Technologies



\* Python

\* MQTT

\* Mosquitto

\* Paho MQTT

\* JSON

\* SQLite

\* NumPy

\* Scikit-learn

\* Joblib

\* Flask

\* Flask-Sock

\* WebSockets

\* JavaScript

\* Three.js

\* HTML/CSS



\## Project Structure



```text

industrial-digital-twin/

│

├── frontend/

│   └── index.html

│

├── python-gateway/

│   ├── gateway.py

│   ├── web\_server.py

│   ├── test\_publisher.py

│   └── failure\_publisher.py

│

├── ml/

│   ├── train\_model.py

│   ├── predict.py

│   └── pump\_anomaly\_model.pkl

│

├── database/

│

├── esp32/

├── plc/

├── opcua/

└── security/

```



\## Current Status



\* \[x] MQTT broker communication

\* \[x] JSON telemetry

\* \[x] Python MQTT gateway

\* \[x] SQLite telemetry storage

\* \[x] ML model training

\* \[x] ML anomaly inference

\* \[x] Three.js Digital Twin

\* \[x] WebSocket telemetry

\* \[ ] ESP32/Wokwi telemetry source

\* \[ ] FreeRTOS tasks

\* \[ ] TinyML deployment

\* \[ ] PLC simulation

\* \[ ] Modbus communication

\* \[ ] OPC UA

\* \[ ] SCADA/HMI integration

\* \[ ] OT cybersecurity monitoring

\* \[ ] Docker deployment

\* \[ ] Linux deployment



\## Purpose



The project is being developed as a practical Industrial Automation portfolio project combining mechanical-engineering domain knowledge with IIoT, software, machine learning, embedded systems and industrial communication technologies.



