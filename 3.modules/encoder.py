class Encoder:




    def on_pulse(self):
        current_A = self.pin_A.value()
        current_B = self.pin_B.value()
        if self.previous_A == None:
            self.previous_A = current_A
        else:
            if  current_A == 1 :
                if   current_B == 0 :
                    self.pulse_count += 1
                else:
                    self.pulse_count -= 1
            if  current_A == 0:
                if   current_B == 1 :
                    self.pulse_count += 1
                else:
                    self.pulse_count -= 1
        self.previous_A = current_A

            