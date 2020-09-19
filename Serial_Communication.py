import time
import schedule
import tkinter as tk
import Car

import Value_Functions as vf


def main_func():
    vf.comm_w_arduino(list_values)
    # Stores Readings in a Master List
    vf.create_master_list(list_values, MASTER_VALUES)


list_values = []
MASTER_VALUES = []
print('Program Started')

schedule.every(1).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(.1)
