from motor import Motor
import time
motor = Motor(16,4,2)
def test_speed(speed,test_name):
    motor.set_speed(speed)
    time.sleep(2)
    assert motor.speed == speed
    if speed == 0 :
        assert motor.is_running == False
    else:
        assert motor.is_running == True
    print(test_name,"通过")
def test_limit(input_speed,expected_speed,test_name):
    motor.set_speed(input_speed)
    time.sleep(2)
    assert motor.speed == expected_speed
    print(test_name,"通过")

test_speed(50,"正转测试")
test_speed(-50,"反转测试")
test_limit(200,100,"边界测试")
motor.stop()
