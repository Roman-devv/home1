import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
ledOut= [0,0,0,0, 0,0,0,0]
dac=[8, 11, 7, 1, 0, 5, 12, 6]
led=[2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT)
gpio.setup(led, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def dec2bin(n):
    return[int (element) for element in bin(n)[2:].zfill(8)]
def bin2dec(n):
    num =0
    s = 7
    for i in range(8):
        num+= n[i]*2**s
        s-=1
    return(num)

def adc():
    DACout= [1,0,0,0, 0,0,0,0]
    gpio.output(dac, DACout)
    for i in range(8):
        time.sleep(0.005)  
        if gpio.input(comp) ==1:
            DACout[i] = 0 
        if i!=7:
            DACout[i+1] = 1  
        gpio.output(dac, DACout) 
        time.sleep(0.005)       
    return(DACout)  

try:
    while True:
        Vn = bin2dec(adc())
        d =(Vn+1)/256

        for i in range(0, int(8*(1-d))):
            ledOut[i] = 0
        for i in range(int(8*(1-d)), 8):
            ledOut[i] = 1   

        gpio.output(led, ledOut)

        if Vn!=0:
            print(Vn*3.6/256,"В")


           

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
    gpio.cleanup() 
