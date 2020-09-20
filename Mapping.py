import tkinter as tk

points_queue = []


class Point:
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        self.size = 4
        self.draw(canvas)

    def draw(self, canvas):
        x = canvas.create_oval(self.x - self.size, self.y - self.size,
                               self.x + self.size, self.y + self.size, fill='red')
        points_queue.append(x)

    def determine_pos(self, canvas, list_values):
        maxd = 750
        counter = 0
        while counter < 3:
            list_values[counter] = ((list_values[counter] * 100) / 2) * 10
            counter += 1
        # Inner sensor data
        dist_inward = list_values[0] + (12.5 / 2) * 10  # Correction factor for width of the car
        # Front sensor data
        dist_forward = list_values[1] + (12.5 / 2) * 10  # Correction factor for the length of the car
        # Outer sensor data
        dist_outward = list_values[2] + (12.5 / 2) * 10
        if (maxd - 2 <= dist_inward <= maxd + 2) and list_values[3] == 1:  # and going east:
            self.x = maxd - dist_forward
            self.y = maxd - (dist_inward+dist_outward)
            self.draw(canvas)
        elif (maxd - 2 <= dist_inward <= maxd + 2) and list_values[3] == 2:  # and going south:
            self.x = maxd - (dist_inward+dist_outward)
            self.y = maxd - dist_forward
            self.draw(canvas)
        elif (maxd - 2 <= dist_inward <= maxd + 2) and list_values[3] == 3:  # and going west
            self.x = maxd - dist_forward
            self.y = maxd - (dist_inward+dist_outward)
            self.draw(canvas)
        elif (maxd - 2 <= dist_inward <= maxd + 2) and list_values[3] == 4:  # and going north
            self.x = maxd - (dist_inward+dist_outward)
            self.y = maxd - dist_forward
            self.draw(canvas)
        elif dist_inward > maxd or dist_inward < 0:
            pass
        else:
            pass

