import serial


def create_master_list(values, MASTER_VALUES):
    MASTER_VALUES.append(values)
    print(MASTER_VALUES)


def comm_w_arduino(list_values):
    arduino = serial.Serial('com3', 9600)
    print('Connection Established')
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
    print(f'Collected readings from Arduino: {list_values}')

    ard_data = 0
    arduino.close()
    print('Connection closed')
    print('<-------------------------------------->')