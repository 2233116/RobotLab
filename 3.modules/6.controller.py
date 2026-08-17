class Controller:
    def __init__(self):
        self.target_speed = 0
        self.output = 0 
    def set_target_speed(self,speed):
        self.target_speed = speed
    def update_output(self):
        self.output = self.target_speed



  