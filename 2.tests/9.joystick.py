from joystick import Joystick
from time import sleep_ms
joystick = Joystick()
while True:
    x,y = joystick.get_values()
    print(x,y)
    sleep_ms(100)
