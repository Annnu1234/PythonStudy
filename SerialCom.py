import serial
import time
from enum import Enum

class WriteReadCTRL(Enum):
    WriteReadParm = 0


# Open the serial port (adjust port name and baud rate as needed)
ser = serial.Serial('COM3', 115200)  # On Windows, use something like 'COM3'
# On Linux, you might use '/dev/ttyUSB0' or '/dev/ttyACM0'

# Wait for the serial port to initialize
time.sleep(2)
print("st")
#if WriteReadCTRL(0).value == 1:
    #while 1:
print("wri")
# Send data over the serial connection
ser.write(b'Hello from Aniruddha!\n')  # Sending a string to the serial port
time.sleep(1)

if WriteReadCTRL(0).value == 0:
     while 1:
        #print("rec")
        #if ser.in_waiting > 0:  # Check if there's data waiting to be read
            received_data = ser.readline()  # Read a line from the serial port work only with \n end of line
            print(f"Received: {received_data.decode('utf-8').strip()}")
        #break
# Close the serial port after communication
ser.close()
