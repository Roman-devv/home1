import RPi.GPIO as gg
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gg.setmode(gg.BCM)
gg.setup(dac, gg.OUT)
#finally
gg.output(dac, 0)
#try
a = 0
t1 = int(input())
while a != "q":
    for a in range(256):
        time.sleep(t1)
        s = bin(a)[2:]
        s = [::-1]
        t = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(s)):
            t[i] = int(s[i])
        t = t[::-1]
        gg.output(dac, t)
        print("voltage =", 3.3*a/256)
    for a in range(255, 0, -1):
        time.sleep(t1)
        s = bin(a)[2:]
        s = [::-1]
        t = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(s)):
            t[i] = int(s[i])
        t = t[::-1]
        gg.output(dac, t)
        print("voltage =", 3.3 * a / 256)
