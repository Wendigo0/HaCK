import tkinter as tk

car_queue = []


class Car:
    def __init__(self, canvas):
        self.x = 20  # Gyro initial Reading
        self.y = 20  # Gyro initial Reading
        self.draw(canvas)

    def draw(self, canvas):
        if len(car_queue) != 0:
            canvas.delete(car_queue[0])
            car_queue.pop()

        x = canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill='blue')
        car_queue.append(x)

    def move(self, canvas):
        pass

