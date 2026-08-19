#DifferentialDrive 计算测试
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
#DifferentialDrive + Motor 完整数据流测试
from motor import Motor
left_motor = Motor(1,2,3)
right_motor = Motor(4,5,6)
controller.set_target_speed(50)
controller.update_output()
differential_drive.set_turn(20)
differential_drive.calculate_wheel_speeds(controller.output)
left_motor.set_speed(differential_drive.left_speed)
right_motor.set_speed(differential_drive.right_speed)



