class ChassisController:
    def __init__(self,max_speed = 100):
        self.max_speed = max_speed
    def mix(self,forward,turn):
        L = forward + turn
        R = forward - turn
        if max(abs(L),abs(R)) > self.max_speed:
            scale = max(abs(L),abs(R))/self.max_speed
            L = L/scale
            R = R/scale
        return L,R
