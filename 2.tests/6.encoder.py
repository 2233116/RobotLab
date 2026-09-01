from encoder import Encoder
from time import sleep
from machine import Pin
pin_A_out = Pin(13,Pin.OUT)
pin_B_out = Pin(2,Pin.OUT)
encoder  = Encoder(12,4,1,1)
a = 0
while True:
    pin_A_out.value(0)
    pin_B_out.value(0)
    sleep(1)
    print(encoder.pulse_count)
    sleep(1)
    pin_A_out.value(0)
    pin_B_out.value(1)
    sleep(1)
    print(encoder.pulse_count)
    sleep(1)
    pin_A_out.value(1)
    pin_B_out.value(1)
    sleep(1)
    print(encoder.pulse_count)
    sleep(1)
    pin_A_out.value(1)
    pin_B_out.value(0)
    sleep(1)
    print(encoder.pulse_count)
    sleep(1)
    pin_A_out.value(0)
    pin_B_out.value(0)
    sleep(1)
    print(encoder.pulse_count)
    sleep(1)
    break
    


