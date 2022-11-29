# Write your code here :-)
import usb_cdc

class CircuitSerial:

    def __init__(self):
        self.__serial = None

    def load(self):
        self.__serial = usb_cdc.data

    def get_data_port(self):
        print(self.__serial)

    def receive(self):
        received = ""
        while self.__serial.in_waiting > 0:
            incoming = self.__serial.read(1)

            if incoming != b'\r':
                received += incoming.decode("utf-8")
            elif incoming == b'\r':
                break
        if received != "":
            return received

    def send(self, id, data):
        self.__serial.write(str.encode("%s: %s%s" % (id,data,"\r")))

