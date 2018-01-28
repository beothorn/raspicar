import serial
import time
import cv2

ser = serial.Serial('/dev/ttyUSB0', 115200)
time.sleep(2)
ser.write(bytearray([0,255,0,255,0,255,0,255]))
time.sleep(1.5)
ser.write(bytearray([0,0,0,0,0,0,0,0]))

camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite('opencv.png', image)
del(camera)
