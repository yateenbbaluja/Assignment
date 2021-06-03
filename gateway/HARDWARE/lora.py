import json
import serial
from CONFIGURATION.config import confi
import time
import random


fre = ["BETA", "ALFA", "GAMMA"]


def get_data():
    DATA = {"id": random.choice(fre),
            "ST": "DHT11",
            "NODE_TYPE": "Sensor",
            "data": {"temprature": random.randint(20, 50), "Humidity": random.randint(70, 90)}}
    return DATA


# while 1:
#     print(get_data())
#     time.sleep(1)

# class LORA:
#     def __init__(self):
#         self.config = confi()
#         self.ser = serial.Serial(port="COM8",
#                                  baudrate= self.config.LORA_PORT_BAUDRATE,
#                                  parity=serial.PARITY_NONE,
#                                  stopbits=serial.STOPBITS_ONE,
#                                  bytesize=serial.EIGHTBITS,
#                                  timeout=self.config.LORA_TIMEOUT)
#         print("connected to: " + self.ser.portstr)
#     def get_data(self):
#         data = self.ser.readline().decode(self.config.LORA_DECODE)
#         if len(str(data)) > self.config.LORA_PACK_LIM:
#             return json.loads(data)
