class MotorController:
    def __init__(self,motor,encoder,pid,target_speed):
        self.motor = motor
        self.encoder = encoder
        self.pid = pid
        self.target_speed = target_speed
        self.control_count = 0
        self.dt = 0
        self.pwm = 0
    def update(self):
        if self.encoder.update():
            self.control_count += 1
            self.dt = self.dt + self.encoder.elapsed_time
            if self.control_count >= 3:
                self.pwm = self.pid.update(self.encoder.current_speed,self.dt,self.target_speed)
                self.control_count = 0
                self.dt = 0
                self.motor.set_speed(self.pwm)
                print("current_speed: \n", self.encoder.current_speed)

