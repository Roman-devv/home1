import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt

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
ho = []
he = []
vo = []
t3 = []
try:
    a1 = time.time()
    while True:
        a = time.time()
        Vn = bin2dec(adc())
        d =(Vn+1)/256

        for i in range(0, int(8*(1-d))):
            ledOut[i] = 0
        for i in range(int(8*(1-d)), 8):
            ledOut[i] = 1   

        gpio.output(led, ledOut)

        if Vn!=0:
            print(Vn*3.6/256,"В")
        
        if Vn > 200:
            gpio.output(troyka, 0)
            break
        b = time.time()
        ho.append(str(b-a))
        vo.append(Vn*3.6/256)

    while True:
        a = time.time()
        gpio.output(troyka, 0)
        Vn = bin2dec(adc())
        if Vn!=0:
            print(Vn*3.6/256,"В")
        if Vn == 0:
            break
        b = time.time()
        ho.append(str(b-a))
        vo.append(Vn*3.6/256)
    b1 = time.time()
    he.append(str(b1-a1))
    print("Время 1 измерения :", ho)
    print("Время всего эксперемента :", he)
    t = [str(i) for i in vo]
    t2 = [float(i) for i in ho]
    t2 = [1/i for i in t2]
    t2 = [str(i) for i in t2]
    print("Частота :", t2)
    plt.plot(vo)
    plt.show()
    with open("data.txt", "w") as f:
        f.write("\n".join(t))
    with open("settings.txt", "w") as f:
        f.write("\n")
        f.write("Дискретизация :")
        f.write("\n")
        f.write("\n".join(t2))
        f.write("\n")
        f.write(" Квантование АЦП :")
        f.write("\n")
        f.write("\n".join(t))


           

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
