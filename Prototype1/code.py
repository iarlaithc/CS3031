from adafruit_circuitplayground import cp
from vibration import Haptics
import time

def check_tilted(xval,yval):
    #---
    # this just checks x and y values to see if its not flat 
    # --#
    if xval > middle_high_threshold or xval < middle_low_threshold or yval > middle_high_threshold or yval < middle_low_threshold:
        return True
    else:
        return False

vibration_motor = Haptics()
#create class instance
#set thresholds for movement
middle_low_threshold = -2
middle_high_threshold = 2
tilted = False

while True:
    #loop to run the checkloop within so to keep the initial start time for each reset
    current_time = time.time()
    prev_time = current_time
    #var to hold current time
    time_threshold = 10
    #10s countdown timer 
    
    loop = True
    while loop == True:
        #loop to run checks until the appropriate checks are met
        current_time = time.time()        
        x = cp.acceleration[0]
        y = cp.acceleration[1]

        if check_tilted(x,y) == True:
            difference = current_time-prev_time
            #compare time now vs OG time
            if difference > time_threshold:
                tilted = True
                loop = False  
                #sets tilted bool to true and ends containing loop 
        else:
            tilted = False          

        if tilted == True:
            #if tilted bool var = true then start vibration
            vibration_motor.start(1)

        elif tilted == False:
            #stop vibration
            vibration_motor.stop()
        
    time.sleep(0.1)