from create_serial import CreateSerial
import keyboard

#this com port is only the one that works for my pc yours could be different
serial_1 = CreateSerial("COM8") # creating an instance of the serial connection
serial_1.recordAvailablePorts()


serial_1.openPort()
data = {}
filtered_data = {}

while True:
    event = keyboard.read_event()
    #this just waits for a keyboard input, its blocks until one is registered
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        user_in = "s"
        if key == "v":
            # v stops vibration, s starts it
            user_in = key
        serial_1.write(user_in)