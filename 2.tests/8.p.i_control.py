from motor import Motor
from encoder import Encoder
from time import sleep
motor = Motor(33,27)
encoder  = Encoder(4,5,22,56)
kp = 0.25
ki = 0.3
kd = 0.05
integral_error = 0
integral_max = 1000
integral_min = -1000
target_speed = 100
control_count = 0
previous_speed = None
base_pwm = target_speed/2
pwm = base_pwm
motor.set_speed(pwm)
while True:
    if encoder.update():
        control_count += 1
        if previous_speed is not None:
            if control_count >= 3:
                    control_count = 0
                    error = target_speed - encoder.current_speed
                    integral_error = integral_error + error*encoder.elapsed_time
                    if integral_error >= integral_max:
                        integral_error = integral_max
                    elif integral_error <= integral_min:
                        integral_error = integral_min
                    P = kp*error
                    I = ki*integral_error
                    D = kd*(previous_speed - encoder.current_speed)/encoder.elapsed_time
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
        error = target_speed - encoder.current_speed
        previous_speed = encoder.current_speed
        print("pwm: \n",pwm)
        print("error: \n",error)
        print("current_speed: \n", encoder.current_speed)








