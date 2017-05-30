from xbee import XBee
import serial

PORT = '/dev/ttyUSB0'
BAUD = 9600

ser = serial.Serial(PORT, BAUD)

xbee = XBee(ser)
# Send the string 'Hello World' to the module with MY set to 1
xbee.send('at',frame_id='A',command='DH')

# Wait for and get the response
print(xbee.wait_read_frame())

ser.close()
