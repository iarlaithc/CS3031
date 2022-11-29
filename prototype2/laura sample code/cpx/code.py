# Write your code here :-)
from adafruit_circuitplayground import cp # refered to access the internal sensors/actuators
from circuit_serial import CircuitSerial
import time

ser = CircuitSerial()
ser.load()

while True:
    data = ser.receive()
    if data != None:
        print(data)
    time.sleep(0.1)


