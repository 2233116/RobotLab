from machine import ADC,Pin
class Joystick:
    def __init__(self):
        self.x_axis = ADC(Pin(34))
        self.y_axis = ADC(Pin(35))
        self.x_axis.atten(ADC.ATTN_11DB)
        self.y_axis.atten(ADC.ATTN_11DB)
        self.x_center = 1791
        self.y_center = 1786
        self.dead_zone = 100
    def read_raw(self):
        x = self.x_axis.read()
        y = self.y_axis.read()
        return x,y
    def process_deadzone(self,value,center):
        if abs(value - center) <= self.dead_zone:
            return 0
        else:
            return value
    def map_axis(self,value,center):
        if self.process_deadzone(value,center) == value:
            if value - center >= 0:
                output = ((value - (center+self.dead_zone))/(4095 - (center+self.dead_zone)))*100
            else:
                output = -(((center-self.dead_zone) - value)/((center-self.dead_zone) - 0))*100
            return output
        else:
            return 0
    def get_values(self):
        x,y = self.read_raw()
        X = self.map_axis(x,self.x_center)
        Y = self.map_axis(y,self.y_center)
        return X,Y