import serial

# Open the serial port. Adjust the device name to match your configuration.
# It might be '/dev/ttyUSB0', '/dev/ttyACM0', or something similar.
ser = serial.Serial('/dev/ttyUSB0', 9600)

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
except KeyboardInterrupt:
    print("Program terminated!")
finally:
    ser.close()
