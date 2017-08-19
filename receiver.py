Code for receiver:
from network import LoRa
import socket
import time
import pycom

pycom.heartbeat(False)
lora = LoRa(mode=LoRa.LORA, frequency=863000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)

while True:
    print(s.recv(64))
    pycom.rgbled(0xff0000)
    time.sleep_ms(1000)
    pycom.rgbled(0x0000)
    time.sleep_ms(1)
