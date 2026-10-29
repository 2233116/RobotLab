from motor import Motor
from encoder import Encoder
from pid import PID
from motorcontroller import MotorController
from dualmotorcontroller import DualMotorController
from time import ticks_ms,ticks_diff
left_motor = Motor(33,27)
right_motor = Motor(13,12)
left_encoder  = Encoder(4,5,22,56)
right_encoder  = Encoder(21,22,22,56)
left_pid = PID(0.25,0.3,0.05)
right_pid = PID(0.25,0.3,0.05)
left_motorcontroller = MotorController(left_motor,left_encoder,left_pid,"left")
right_motorcontroller = MotorController(right_motor,right_encoder,right_pid,"right")
dual = DualMotorController(left_motorcontroller,right_motorcontroller)
dual.set_targets(60,90)
stage = 0
stage_start = ticks_ms()
try:
    while True:
        time = ticks_ms()
        elapsed = ticks_diff(time,stage_start)
        dual.update()
        if stage == 0 and elapsed >= 5000:
            dual.set_targets(90,60)
            stage = 1
            stage_start = time
        elif stage == 1 and elapsed >= 5000:
            dual.set_targets(0,0)
            stage = 2
            stage_start = time
        elif stage == 2 and elapsed >= 5000:
            dual.set_targets(60,60)
            stage = 3
            stage_start = time
finally:
    dual.stop()
   
    
     



