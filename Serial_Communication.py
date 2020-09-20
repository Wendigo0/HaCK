import tkinter as tk

from Car import Car
from Mapping import Point
import Value_Functions as vf

window = tk.Tk()
canvas = tk.Canvas(window, width=750, height=750, bg='black')  # Make 1pixel = 2cm
canvas.pack()
car = Car(canvas)

counter = 0
list_values = []
MASTER_VALUES = []


def main():

    # Gathers reading from arduino distance sensors
    vf.comm_w_arduino(list_values)
    # Stores Readings in a Master List
    print(list_values)

    # Car moves based on the IMU reading
    car.move(canvas, list_values)

    window.bind("<space>", lambda event: vf.pause(event))

    dots = Point(canvas)
    dots.determine_pos(canvas, list_values)

    window.after(10, main)


# print('Program Started')

main()
window.mainloop()
