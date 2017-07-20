from xbee import XBee
import serial

def main():
    try:
        ser = serial.Serial('/dev/tty.usbserial-AL01T2SX',9600)
        
        xbee = XBee(ser)

        xbee.send('at',frame_id='A',command='DH')

        response = xbee.wait_read_frame()

    except KeyboardInterrupt:
        pass
    finally:
        ser.close()

if __name__ == '__main__':
    main()
