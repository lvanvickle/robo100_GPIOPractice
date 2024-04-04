import serial

# Open serial port.
ser = serial.Serial('/dev/ttyUSB0', 9600)

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(f"Distance: {data} cm")
except KeyboardInterrupt:
    print("Program terminated!")
finally:
    ser.close()
