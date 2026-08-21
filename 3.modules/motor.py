from machine import Pin,PWM
FORWARD  =  1
BACKWARD = 2
STOP = 3
class Motor:
    def __init__(self,pin_num_1,pin_num_2,pin_num_3) :
        self.pin1 = Pin(pin_num_1,Pin.OUT)
        self.pin2 = Pin(pin_num_2,Pin.OUT)
        self.pwm = PWM(Pin(pin_num_3),freq = 1000) 
        self.speed = 0
        self.is_running = 0
    def stop(self):
        self.set_speed(0)
    def set_speed(self,speed):
        if speed  > 100:
            speed = 100
        elif speed < -100 :
            speed = -100
        if speed == self.speed :
            return
        if speed > 0 :
            self.pin1.value(1)
            self.pin2.value(0)
            self.is_running = True
        elif speed < 0 :
            self.pin1.value(0)
            self.pin2.value(1) 
            self.is_running = True
        elif speed == 0 :
            self.pin1.value(0)
            self.pin2.value(0)
            self.is_running = False
        speed_1 = abs(speed)
        self.speed = speed
        self.pwm.duty_u16(int(speed_1/100*65535))
        
     