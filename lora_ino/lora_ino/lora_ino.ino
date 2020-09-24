#include  <SoftwareSerial.h>  
SoftwareSerial Lora(11, 10); // RX | TX  
/*
  AT+ADDRESS=your_address (0~65535)
  AT+PARAMETER=12,7,1,4
  AT+IPR=your_baudrate
  AT+NETWORKID=your_netwokid (0~16)
  AT+CPIN=your_password (32 char long)
  */
void setup()  
{  
  Serial.begin(9600);  
  Serial.println("Enter AT commands:");  
  Lora.begin(9600);  // default speed 115200
}  
void loop()  
{  
  // Keep reading from Lora and send to Arduino Serial Monitor  
if (Lora.available())  
  {  
    Serial.write(Lora.read());
  }  
  // Keep reading from Arduino Serial Monitor and send to Lora
  if (Serial.available())  
  {  
    Lora.write(Serial.read());  
  }  
}  
