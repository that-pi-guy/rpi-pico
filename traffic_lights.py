from machine import Pin
import time

# Declare GPIO in use
ledRed = Pin(18, Pin.OUT)
ledYellow = Pin(19, Pin.OUT)
ledGreen = Pin(20, Pin.OUT)

# Traffic Light Sequence in a Tuple
tplStop = (1, 0, 0)
tplReadyGo = (1, 1, 0)
tplGo = (0, 0, 1)
tplReadyStop = (0, 1, 0)
tplReset = (0, 0, 0)

# A Tuple of Tuple
tplSequence = (tplStop, tplReadyGo, tplGo, tplReadyStop, tplStop, tplReset)

# While Counter Init
icount = 0

while icount < 6:   
    ledRed.value(tplSequence[icount][0])
    ledYellow.value(tplSequence[icount][1])
    ledGreen.value(tplSequence[icount][2])
    time.sleep(1.5)
    icount += 1