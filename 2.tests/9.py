previous_speed = None
stable_count = 0
if previous_speed is not None:
    if abs(previous_speed - encoder.current_speed) <= 2:
        stable_count += 1
        if stable_count == 3:
            stable_count = 2
    else:
        stable_count = 0
previous_speed = encoder.current_speed