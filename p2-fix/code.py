from keyboard import is_pressed
from vibration import Haptics
import time

vibration_motor = Haptics()

while True:
	if keyboard.is_pressed("v"):
		vibration_motor.start(1)

	if keyboard.is_pressed("s"):
		vibration_motor.start()
	
	time.sleep(0.1)
