import tkinter as tk

car_queue = []


class Car:
    def __init__(self, canvas):
        self.x = 20  # 40 cm from back(left)
        self.y = 20  # 40 cm from side(top)
        self.size = 12.5/2
        self.draw(canvas)

    def draw(self, canvas):
        if len(car_queue) != 0:
            canvas.delete(car_queue[0])
            car_queue.pop()

        x = canvas.create_rectangle(self.x - self.size, self.y - self.size,
                                    self.x + self.size, self.y + self.size, outline='blue')
        car_queue.append(x)

    def move(self, canvas, master_list):
        maxd = 750
        counter = 0
        while counter < 3:  # Scale the meter data to pixel data
            master_list[counter] = (master_list[counter]*100)/2
            counter += 1

        dist_inward = master_list[0] + 12.5/2
        dist_forward = master_list[1] + 12.5/2
        dist_outward = master_list[2] + 12.5/2

        if master_list[3] == 1:  # North wall
            self.x = maxd - dist_forward
            self.y = dist_outward
            self.draw(canvas)
        elif master_list[3] == 2:  # East wall
            self.x = maxd - dist_outward
            self.y = maxd - dist_forward
            self.draw(canvas)
        elif master_list[3] == 3:  # South wall
            self.x = dist_forward
            self.y = maxd-dist_outward
            self.draw(canvas)
        elif master_list[4] == 4:  # West wall
            self.x = dist_outward
            self.y = dist_forward
            self.draw(canvas)
