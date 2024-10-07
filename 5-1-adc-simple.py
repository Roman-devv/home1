import RPi.GPIO as gg
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
gg.setmode(gg.BCM)
gg.setup(dac, gg.OUT, initial=gg.LOW)

gg.setup(troyka, gg.OUT, initial=gg.HIGH)

gg.setup(comp, gg.IN)

def f(m):
    s = bin(m)[2:]
    s = s[::-1]
    t = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(s)):
        t[i] = int(s[i])
    t = t[::-1]
    return t

def adc():
    for u in range(256):
        signal = f(u)
        gg.output(dac, signal)
        time.sleep(0.01)
        compv = gg.input(comp)
        if compv == 1:
            return u
    return 0

#try
while True:
    t = adc()
    print(t, 3.3/256*t)
#finally
gg.output(dac, 0)
gg.cleanup()(dac)