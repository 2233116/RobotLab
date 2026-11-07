from joystick import Joystick
from chassiscontroller import ChassisController
from time import sleep_ms
joystick = Joystick()
chassiscontroller = ChassisController()
while True:
    x,y = joystick.get_values()
    forward = -y
    turn = -x
    L,R = chassiscontroller.mix(forward,turn)
    print(L,R)
    sleep_ms(100)

