
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
        new_list = list_values.copy()
        while counter < 3:
            new_list[counter] = ((new_list[counter] * 100) / 2) * 10
            counter += 1
        new_list[3] = int(new_list[3])
        # Inner sensor data
        dist_inward = new_list[0] + (12.5 / 2) * 10  # Correction factor for width of the car
        # Front sensor data
        dist_forward = new_list[1] + (12.5 / 2) * 10  # Correction factor for the length of the car
        # Outer sensor data
        dist_outward = new_list[2] + (12.5 / 2) * 10

        if new_list[3] == 1:  # and going east:
            self.x = maxd - dist_forward
            self.y = dist_inward + dist_outward
            self.draw(canvas)
        elif new_list[3] == 2:  # and going south:
            self.x = maxd - (dist_inward+dist_outward)
            self.y = maxd - dist_forward
            self.draw(canvas)
        elif new_list[3] == 3:  # and going west
            self.x = dist_forward
            self.y = maxd - (dist_inward+dist_outward)
            self.draw(canvas)
        elif new_list[3] == 4:  # and going north
            self.x = dist_inward + dist_outward
            self.y = dist_forward
            self.draw(canvas)
        elif dist_inward > maxd or dist_inward < 0:
            pass
        else:
            pass
