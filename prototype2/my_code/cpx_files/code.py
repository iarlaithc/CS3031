from circuit_serial import CircuitSerial
import time
from vibration import Haptics 

vibration_motor = Haptics()
vibration_set = False
ser = CircuitSerial()
ser.load()

while True:
    #waits for serial message
    data = ser.receive()
    if data != None:
        if data == "v":
            vibration_motor.start(1)
        if data == "s":
            vibration_motor.stop()

    time.sleep(0.1)


