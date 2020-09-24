# Lora  

## 校正
If you recieve different message, try modify the lora baudrate to 9600.\
RYLR896在用預設baudrate 115200下接收端常常會收到跟傳輸不一樣的值，改用baudrate 9600情況就會改善。\
可透過下面指令更改

#### *Python script*
```Python
from Lora import lora
_lora = lora(init=True)
```
or

#### *AT command*

    AT+IPR=9600

#### 
## 接線

| **Arduino Side** | **Raspberry Pi Side** |
| :---------: | :---------: |
|![](https://github.com/boy07132004/Lora/blob/master/ArduinoSide.PNG)|![](https://github.com/boy07132004/Lora/blob/master/PiSide.PNG)|
