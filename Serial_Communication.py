import tkinter as tk
import serial
import time

from Car import Car
from Mapping import Point
import Value_Functions as vf

window = tk.Tk()
canvas = tk.Canvas(window, width=750, height=750, bg='black')  # Make 1pixel = 2cm
canvas.pack()
car = Car(canvas)
dots = Point(canvas)

arduino = serial.Serial("com3", 9600, timeout=2)  # Establishes the connection
time.sleep(1)
list_values = []
MASTER_VALUES = []


def main():

    # Gathers reading from arduino distance sensors
    vf.comm_w_arduino(arduino, list_values)

    # Prints values for reference
    print(list_values)
    
    if len(list_values) == 4:
        # Car moves based on the distance sensor readings
        car.move(canvas, list_values)

        # Pauses the code with the map still showing
        window.bind("<space>", lambda event: vf.pause(event))

        dots.determine_pos(canvas, list_values)

    window.after(10, main)

# print('Program Started')


main()
window.mainloop()
