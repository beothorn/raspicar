import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

STOPPED = 0
FORWARD = 1
BACKWARD = 2

latch_pin = 3 #arduino 12
clock_pin = 4 #arduino 4
motor_enable_pin = 14 #arduino 7
serial_data_pin = 15 #arduino 8

GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(motor_enable_pin, GPIO.OUT)
GPIO.setup(serial_data_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)

def write_serial_bit(output):
    GPIO.output(clock_pin, GPIO.LOW)
    GPIO.output(serial_data_pin, output)
    GPIO.output(clock_pin, GPIO.HIGH)

def write_serial_given_bool(condition):
    if condition:
        write_serial_bit(GPIO.HIGH)
    else:
        write_serial_bit(GPIO.LOW)


def send_state_to_shield(motors_state):
    GPIO.output(latch_pin, GPIO.LOW)
    GPIO.output(serial_data_pin, GPIO.LOW)
    
    swrite(motors_state.motor3 == BACKWARD)
    swrite(motors_state.motor4 == BACKWARD)
    swrite(motors_state.motor3 == FORWARD)
    swrite(motors_state.motor2 == BACKWARD)
    swrite(motors_state.motor1 == BACKWARD)
    swrite(motors_state.motor1 == FORWARD)
    swrite(motors_state.motor2 == FORWARD)
    swrite(motors_state.motor4 == FORWARD)

    GPIO.output(latch_pin, GPIO.HIGH)
    

current_latch_state = { 
    motor1 : STOPPED,
    motor2 : STOPPED,
    motor3 : STOPPED,
    motor4 : STOPPED
}

send_state_to_shield(current_latch_state)

GPIO.output(motor_enable_pin, GPIO.LOW)

