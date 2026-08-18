from controller import Controller
from differential_drive import Differentialdrive
controller = Controller()
differential_drive = Differentialdrive()
controller.set_target_speed(50)
assert controller.target_speed == 50
print("测试通过")
controller.update_output()
assert controller.output == 50
print("测试通过")
differential_drive.set_turn(20)
assert differential_drive.turn == 20
print("测试通过")
differential_drive.calculate_wheel_speeds(controller.output)
assert differential_drive.left_speed == 70
assert differential_drive.right_speed == 30
print("成功右转")