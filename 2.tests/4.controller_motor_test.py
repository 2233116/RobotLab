from controller import Controller
from motor import Motor
controller = Controller()
motor_a = Motor(16,4,2,)
motor_b = Motor(1,4,5,)
controller.set_target_speed(50)
assert controller.target_speed == 50
print("检查通过")
controller.update_output()
assert controller.target_speed == 50
print("检查通过")
motor_a.set_speed(controller.output)
motor_b.set_speed(controller.output)

