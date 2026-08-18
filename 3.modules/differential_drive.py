class Differentialdrive:
    def __init__(self):
        self.turn = 0
        self.left_speed = 0
        self.right_speed = 0
    def set_turn(self,speed):
        self.turn = speed
    def calculate_wheel_speeds(self,output):
        self.left_speed = output + self.turn
        self.right_speed = output - self.turn