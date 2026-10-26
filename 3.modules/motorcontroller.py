class MotorController:
    def __init__(self,motor,encoder,pid,name):
        self.motor = motor
        self.encoder = encoder
        self.pid = pid
        self.target_speed = 0
        self.name = name
        self.control_count = 0
        self.dt = 0
        self.pwm = 0
        self.was_stopped = 0
    def update(self):
        if self.target_speed == 0 :
            if self.was_stopped == 0:
                self.motor.set_speed(self.target_speed)
                self.pid.reset()
                self.control_count = 0
                self.dt = 0
                self.was_stopped += 1
                print(self.name,"stop")
        else:
            self.was_stopped = 0
            if self.encoder.update():
                self.control_count += 1
                self.dt = self.dt + self.encoder.elapsed_time
                if self.control_count >= 3:
                    self.pwm = self.pid.update(self.encoder.current_speed,self.dt,self.target_speed)
                    self.control_count = 0
                    self.dt = 0
                    self.motor.set_speed(self.pwm)
                    print(f"{self.name}.current_speed: \n", self.encoder.current_speed)
                    print(f"{self.name}.target_speed: \n", self.target_speed)
                    print(f"{self.name}.pwm: \n", self.pwm)



