from controller import Controller
from motor import Motor
controller = Controller()
motor = Motor(16,4,2,)
controller.set_target_speed(50)
assert controller.target_speed == 0
print("检查通过")
controller.update_output()
assert controller.target_speed == 50
print("检查通过")
motor.set_speed(controller.output)

