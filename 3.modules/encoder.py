class Encoder:
    def __init__(self,pin_num_A,pin_num_B,counts_per_rev,gear_ratio):
        self.pin_A = Pin(pin_num_A,Pin.IN,Pin.PULL_UP)
        self.pin_B = Pin(pin_num_B,Pin.IN,Pin.PULL_UP)
        self.counts_per_rev = counts_per_rev
        self.gear_ratio = gear_ratio
        self.start_time = None
        self.pulse_count = 0
        self.current_speed = 0
        self.pin_A.irp(
                     trigger = Pin.IRQ_RISING|Pin.IRQ_FALLING,
                     handler = self.on_pulse
                )

    def on_pulse(self):
        current_A = self.pin_A.value()
        current_B = self.pin_B.value()
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

    def update(self):
        self.current_time = time.time()
        if self.start_time is None:
            self.start_time = self.current_time
            return
        else:     
            self.elapsed_time = self.current_time - self.start_time
            if self.elapsed_time >= 0.2 :
                irq_state = machine.disable_irq()
                local_count =  self.pulse_count
                self.pulse_count = 0
                machine.enable_irq(irq_state)
                self.current_speed = local_count/self.counts_per_rev/self.elapsed_time*60/self.gear_ratio
                self.start_time = self.current_time
            else:
                return
    def get_current_speed(self):
        return self.current_speed
