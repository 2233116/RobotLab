from encoder import Encoder
from time import sleep
from motor import Motor
motor = Motor(33,27)
encoder  = Encoder(4,5,22,56)
previous_speed = None
stable_count = 0
motor.set_speed(40)
while True:
    if encoder.update():
        if previous_speed is not None:
            if abs(previous_speed - encoder.current_speed) <= 2:
                stable_count += 1
                if stable_count == 3:
                    stable_count = 2
                    print("稳定")
            else:
                stable_count = 0
                print(encoder.current_speed)
        previous_speed = encoder.current_speed
    sleep(0.1)

