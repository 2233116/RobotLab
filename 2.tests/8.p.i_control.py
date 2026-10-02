from motor import Motor
from encoder import Encoder
from time import sleep
motor = Motor(33,27)
encoder  = Encoder(4,5,22,56)
kp = 0.25
ki = 0.03
kd = 0
integral_error = 0
integral_max = 1000
integral_min = -1000
target_speed = 100
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
                    integral_error = integral_error + error
                    if integral_error >= integral_max:
                        integral_error = integral_max
                    elif integral_error <= integral_min:
                        integral_error = integral_min
                    P = kp*error
                    I = ki*integral_error
                    D = kd*(previous_speed - encoder.current_speed)/encoder.elapsed_time
                    print("stable_count: \n", stable_count)
                    print("integral_error: \n", integral_error)
                    print("P: \n",P)
                    print("I: \n",I)
                    print("D: \n",D)
                    pwm = base_pwm + P + I + D
                    if pwm > 100:
                        pwm = 100
                    elif pwm < 0:
                        pwm = 0
                    motor.set_speed(pwm)
            else:
                stable_count = 0
        error = target_speed - encoder.current_speed
        previous_speed = encoder.current_speed
        print("pwm: \n",pwm)
        print("error: \n",error)
        print("current_speed: \n", encoder.current_speed)
    sleep(0.2)








