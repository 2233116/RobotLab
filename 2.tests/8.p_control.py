from motor import Motor
from encoder import Encoder
from time import sleep
motor = Motor(33,27)
encoder  = Encoder(4,5,22,56)
kp = 0.1
target_speed = 50
base_pwm = target_speed/2
motor.set_speed(base_pwm)
while True:
    if encoder.update():
        error = target_speed - encoder.current_speed
        pwm = base_pwm + kp*error
        if pwm > 100:
            pwm = 100
        elif pwm < 0:
            pwm = 0
        motor.set_speed(pwm)
        print("pwm: \n",pwm)
        print("error: \n",error)
        print("current_speed: \n", encoder.current_speed)
    sleep(0.2)





