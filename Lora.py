import serial
import time
class lora:
    def __init__(self,port="/dev/ttyS0",baudrate=9600,init=False):
        if init:self.init_lora_device(port)
        self.ser = serial.Serial(port,baudrate=baudrate,timeout=0.5)
        self.AT_command("AT+ADDRESS=6",time_sleep=0.2)
        self.AT_command("AT+PARAMETER=12,7,1,4",time_sleep=0.2)
        self.AT_command("AT+IPR=9600",time_sleep=0.2)
        self.AT_command("AT+NETWORKID=6",time_sleep=0.2)
        #self.AT_command(self.ser,"AT+CPIN?")
        
    def AT_command(self,cmd,time_sleep=1):
        # check AT command format
        cmd = cmd if cmd[-2:]=="\r\n" else cmd+"\r\n"
        self.ser.write(cmd.encode())
        time.sleep(time_sleep)
        print(f"{cmd.split('=')[0][3:]} > {self.ser.read(10).decode('UTF-8')}")
    
    def send(self,message,address=713):
        length = len(str(message))
        self.AT_command(f"AT+SEND={address},{length},{message}\r\n")
    
    def init_lora_device(self,port):
        s = serial.Serial(port,baudrate=115200)
        s.write("AT+IPR=9600\r\n".encode())
        print(f"init Done")
        s.close()
        time.sleep(1)
    def close(self):
        self.ser.close()
    
    
        
        
if __name__ == "__main__" :
    _lora = lora(init=True)
    for _ in range(10): _lora.send("send to 713")
    _lora.close()
    