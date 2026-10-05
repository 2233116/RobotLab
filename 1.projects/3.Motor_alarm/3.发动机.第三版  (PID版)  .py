from motor import Motor
from encoder import Encoder
from pid import PID
motor = Motor(33,27)
encoder  = Encoder(4,5,22,56)
pid = PID(0.25,0.3,0.05)
control_count = 0
target_speed = 100
time_count = 0
motor.set_speed(target_speed/2)
while True:
    if encoder.update():
        control_count += 1
        time_count = time_count + encoder.elapsed_time
        if control_count >= 3:
            dt = time_count
            pwm = pid.update(encoder.current_speed,dt,target_speed)
            control_count = 0
            time_count = 0
            motor.set_speed(pwm)
            print("pwm: \n",pwm)
            print("dt: \n",dt)
        print("current_speed: \n", encoder.current_speed)