class DualMotorController:
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def update(self):
        self.left.update()
        self.right.update()
    def set_targets(self,left_speed,right_speed):
        self.left.target_speed = left_speed
        self.right.target_speed = right_speed


