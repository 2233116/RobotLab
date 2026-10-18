from motor import Motor
from encoder import Encoder
from pid import PID
left_motor = Motor(33,27)
right_motor = Motor(13,12)
left_encoder  = Encoder(4,5,22,56)
right_encoder  = Encoder(21,22,22,56)
left_pid = PID(0.25,0.3,0.05)
right_pid = PID(0.25,0.3,0.05)
left_control_count = 0
right_control_count = 0
left_dt = 0
right_dt = 0
target_speed = 100
left_motor.set_speed(target_speed/2)
right_motor.set_speed(target_speed/2)
while True:
    if left_encoder.update():
        left_control_count += 1
        left_dt = left_dt + left_encoder.elapsed_time
        if left_control_count >= 3:
            left_pwm = left_pid.update(left_encoder.current_speed,left_dt,target_speed)
            left_control_count = 0
            left_dt = 0
            left_motor.set_speed(left_pwm)
            print("left_pwm: \n",left_pwm)
            print("left_integral_error: \n",left_pid.integral_error)
        print("left_current_speed: \n", left_encoder.current_speed)
    if right_encoder.update():
        right_control_count += 1
        right_dt = right_dt + right_encoder.elapsed_time
        if right_control_count >= 3:
            right_pwm = right_pid.update(right_encoder.current_speed,right_dt,target_speed)
            right_control_count = 0
            right_dt = 0
            right_motor.set_speed(right_pwm)
            print("right_pwm: \n",right_pwm)
            print("right_integral_error: \n",right_pid.integral_error)
        print("right_current_speed: \n", right_encoder.current_speed)