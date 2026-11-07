from motor import Motor
from encoder import Encoder
from pid import PID
from motorcontroller import MotorController
from dualmotorcontroller import DualMotorController
from joystick import Joystick
from chassiscontroller import ChassisController
from time import sleep_ms
joystick = Joystick()
chassiscontroller = ChassisController()
left_motor = Motor(33,27)
right_motor = Motor(13,12)
left_encoder  = Encoder(4,5,22,56)
right_encoder  = Encoder(21,22,22,56)
left_pid = PID(0.25,0.3,0.05)
right_pid = PID(0.25,0.3,0.05)
left_motorcontroller = MotorController(left_motor,left_encoder,left_pid,"left")
right_motorcontroller = MotorController(right_motor,right_encoder,right_pid,"right")
dual = DualMotorController(left_motorcontroller,right_motorcontroller)
try:
    while True:
        x,y = joystick.get_values()
        forward = -x
        turn = -y
        L,R = chassiscontroller.mix(forward,turn)
        dual.set_targets(L,R)
        dual.update()
        sleep_ms(100)
finally:
    dual.stop()
   
    
     




