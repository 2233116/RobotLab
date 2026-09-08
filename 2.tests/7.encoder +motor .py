from encoder import Encoder
from time import sleep
from machine import Pin
from motor import Motor
motor = Motor(33,27)
encoder  = Encoder(16,5,22,56)
motor.set_speed(40)#"是否修改名字变成set_pwm"
while True:
    encoder.update()
    print(encoder.current_speed)
    sleep(0.1)
