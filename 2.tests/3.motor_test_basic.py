from motor import Motor
import time 
motor = Motor(13,14,26)
motor.set_speed(50)
time.sleep(5)
print("正转测试结束")
motor.stop()
time.sleep(2)

motor.set_speed(-50)
time.sleep(5)
print("反转测试结束")
motor.stop()
time.sleep(2)

motor.set_speed(100)
time.sleep(5)
print("边界测试结束")
motor.stop()
time.sleep(2)

