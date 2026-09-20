from motor import Motor
from encoder import Encoder
from time import sleep
motor = Motor(33,27)
encoder  = Encoder(4,5,22,56)
kp = 0.1
target_speed = 50
previous_speed = None
stable_count = 0
base_pwm = target_speed/2
pwm = base_pwm
motor.set_speed(pwm)
while True:
    if encoder.update():
        if previous_speed is not None:
            if abs(previous_speed - encoder.current_speed) <= 2:
                stable_count += 1
                if stable_count == 3:
                    stable_count = 2
                    error = target_speed - encoder.current_speed
                    pwm = base_pwm + kp*error
                    if pwm > 100:
                        pwm = 100
                    elif pwm < 0:
                        pwm = 0
                    motor.set_speed(pwm)
            else:
                stable_count = 0
        previous_speed = encoder.current_speed
        error = target_speed - encoder.current_speed
        print("pwm: \n",pwm)
        print("error: \n",error)
        print("current_speed: \n", encoder.current_speed)
    sleep(0.2)





