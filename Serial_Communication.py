import time
import schedule
import tkinter as tk

from Car import Car
import Value_Functions as vf

window = tk.Tk()
canvas = tk.Canvas(window, width=1920, height=1080, bg='black')
canvas.pack()
car = Car(canvas)


def main():

    # Gathers reading from arduino distance sensors
    vf.comm_w_arduino(list_values)
    # Stores Readings in a Master List
    vf.create_master_list(list_values, MASTER_VALUES)

    # Car moves based on the IMU reading
    car.move(canvas, MASTER_VALUES)

    window.after(10, main)


list_values = []
MASTER_VALUES = []

# print('Program Started')

main()
window.mainloop()
