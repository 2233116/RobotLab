class PID:
    def __init__(self,kp,ki,kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral_error = 0
        self.integral_max = 1000
        self.integral_min = -1000
        self.previous_speed = None
    def update(self,current_speed,dt,target_speed):
                    base_pwm = target_speed/2
                    error = target_speed - current_speed
                    self.integral_error = self.integral_error + error*dt
                    if self.integral_error >= self.integral_max:
                        self.integral_error = self.integral_max
                    elif self.integral_error <= self.integral_min:
                        self.integral_error = self.integral_min
                    P = self.kp*error
                    I = self.ki*self.integral_error
                    if self.previous_speed is  None:
                        D = 0
                    else:
                        D = self.kd*(self.previous_speed - current_speed)/dt
                    pwm = base_pwm + P + I + D
                    if pwm > 100:
                        pwm = 100
                    elif pwm < 0:
                        pwm = 0
                    self.previous_speed = current_speed
                    return pwm




