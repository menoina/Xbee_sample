from xbee import XBee
import serial

PORT = '/dev/tty.usbserial-AL01T2SX'
BAUD = 9600

ser = serial.Serial(PORT, BAUD)

xbee = XBee(ser)
# Send the string 'Hello World' to the module with MY set to 1
#xbee.send('at',frame_id='A',command='DH',data='hello World')
#xbee.tx(dest_addr='\x00\x01', data='Hello World')
'''
xbee.send('at', 
        frame_id='A',
        temp='23',
        humi='67',
        options='\x02',
        command='D0',
        parameter='\x02')
'''
xbee.send('at', frame_id='A', command='DH')

# Wait for and get the response
print(xbee.wait_read_frame())

ser.close()
