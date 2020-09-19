import time
import schedule
import tkinter as tk

from Car import Car
import Value_Functions as vf


def main():

    window = tk.Tk()
    canvas = tk.Canvas(window, width=1920, height=1080, bg='black')
    canvas.pack()
    # Gathers reading from arduino distance sensors
    vf.comm_w_arduino(list_values)
    # Stores Readings in a Master List
    vf.create_master_list(list_values, MASTER_VALUES)

    car = Car(canvas)

    window.bind('<KeyPress-a>', lambda event: car.move(event, canvas, MASTER_VALUES))




list_values = []
MASTER_VALUES = []
# print('Program Started')

schedule.every(.5).seconds.do(main)

while True:
    main()
    time.sleep(.1)
