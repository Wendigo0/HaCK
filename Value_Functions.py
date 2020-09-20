import serial
import pdb
from Car import Car


def comm_w_arduino(arduino, list_values):
    # Com for data transfer
    # arduino = serial.Serial('com3', 9600, timeout=2)  # Change the com to the one you want to use
    # print('Connection Established')
    ard_data = arduino.readline()

    list_values.clear()
    decoded_value = str(ard_data[0:len(ard_data)].decode('utf-8'))
    # Remove the random new line formatting
    decoded_value = [x.rstrip() for x in decoded_value]
    new = ''
    # Put the string back together
    for x in decoded_value:
        new += x

    # Turn string into float
    new = new.split(',')

    for x in new:
        list_values.append(float(x))
    # print(f'Collected readings from Arduino: {list_values}')

    ard_data = 0
    # print('<-------------------------------------->')
    # arduino.close()


def counter(counter):
    counter += 1
    return counter


def pause(event=None):
    pdb.set_trace()
