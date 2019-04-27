import serial
from time import sleep

ser = serial.Serial(

    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)
ser.write(bytes('SD2$0D', encoding='ascii'))  # Configure for FDX-B/HDX
x = ser.readline()  # Check for errors
print(x)
sleep(5)  # 5 second delay
ser.write(bytes('RAT$0D', encoding='ascii'))  # Tell RFID bpard to read chip
x = ser.readline()  # Read output
print(x)