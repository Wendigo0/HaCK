import serial
import time
import schedule


list_values = []
list_float_values = []


def comm_w_arduino():
    arduino = serial.Serial('com3', 9600)
    print('Connection Established')
    ard_data = arduino.readline()

    decoded_value = str(ard_data[0:len(ard_data)].decode('utf-8'))
    # Remove the random new line formatting
    decoded_value = [x.rstrip() for x in decoded_value]
    new = ''
    # Put the string back together
    for x in decoded_value:
        new += x
        
    decoded_value = new
    list_values.append(decoded_value)
    print(list_values)
    print(f'Collected readings from Arduino: {list_values}')

    ard_data = 0
    list_values.clear()
    list_float_values.clear()
    arduino.close()
    print('Connection closed')
    print('<-------------------------------------->')


print('Program Started')

schedule.every(1).seconds.do(comm_w_arduino)

while True:
    schedule.run_pending()
    time.sleep(1)
