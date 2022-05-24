from dataclasses import dataclass
from http import client
from wsgiref import headers
from iot_device import Sensor
import json
import time

# object creation of a HTTPConnection
conn = client.HTTPConnection(host="localhost", port=5000)

# class sensor created
s = Sensor()

# simulate de json that will be sent to the server
headers = {'Content-type': 'application/json'}

while True:
    data = {
    "id": 1,
    "name": "Temp_sensor",
    "value": s.get_random_number()
    }
    json_data = json.dumps(data)

    conn.request("POST", "/devices", json_data, headers)
    conn.close()

    print(s.get_random_number())
    time.sleep(1)