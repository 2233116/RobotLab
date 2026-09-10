from motor import Motor
from encoder import Encoder
from time import sleep
motor = Motor(33,27)
encoder  = Encoder(16,5,22,56)
kp = 0.1
pwm = 20
target_speed = 50
while True:
    motor.set_speed(pwm)
    if encoder.update():
        error = target_speed - encoder.current_speed
        pwm = pwm + kp*error
        if pwm > 100:
            pwm = 100
        elif pwm < 0:
            pwm = 0
        print("pwm: \n",pwm)
        print("error: \n",error)
        print("current_speed: \n", encoder.current_speed)
    sleep(0.2)





