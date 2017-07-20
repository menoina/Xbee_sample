from xbee import XBee
import serial

PORT = '/dev/tty.usbserial-AL01T0RJ'
BAUD_RATE = 9600

ser = serial.Serial(PORT,BAUD_RATE)

xbee = XBee(ser)

while True:
    try:
        response = xbee.wait_read_frame()
        print(response)
    except KeyboardInterrupt:
        break
ser.close()
