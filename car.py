print ("Hello World")

class cars:

    def __init__(self):
        current_speed = 1
        max_speed = 1
        fuel_level = 100

        if current_speed > max_speed:
            current_speed = max_speed
            max_speed = current_speed
            fuel_level = max_speed
