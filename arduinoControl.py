import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)
ser.write(bytearray([0,255,0,255,0,255,0,255]))
