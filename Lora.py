import serial
import time
def AT_command(ser,cmd,time_sleep=0.2):
    cmd = cmd if cmd[-2:]=="\r\n" else cmd+"\r\n"
    ser.write(cmd.encode())
    time.sleep(time_sleep)
    print(f"{cmd.split('=')[0][3:]} > {ser.read(10).decode('UTF-8')}")
    
s = serial.Serial("/dev/ttyUSB0",baudrate=9600,timeout=0.5)
AT_command(s,"AT+ADDRESS=6")
AT_command(s,"AT+PARAMETER=12,7,1,4")
AT_command(s,"AT+IPR=9600")
AT_command(s,"AT+NETWORKID=6")
AT_command(s,"AT+CPIN=6A016A016A016A016A016A016A016A01")
while True:
    AT_command(s,"AT+SEND=713,7,@13__7@\r\n",time_sleep=1)
s.close()