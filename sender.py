from network import LoRa
import socket
import time
import pycom

lora = LoRa(mode=LoRa.LORA, frequency=863000000)
pycom.heartbeat(False)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

while True:
    s.send('Pong')
    pycom.rgbled(0x00ff00)
    time.sleep_ms(1000)
    pycom.rgbled(0x000000)
    time.sleep_ms(29000)
