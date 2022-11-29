# Write your code here :-)
import analogio
import board

class Haptics:

    def __init__(self):
        self.__vibration = analogio.AnalogOut(board.A0)

    def start(self, intensity):
        if intensity > 1:
            intensity = 1
        elif intensity < 0:
            intensity = 0

        #self.__vibration.value = round(65535 * intensity)
        self.__vibration.value = 65535

    def stop(self):
        self.__vibration.value = 0

