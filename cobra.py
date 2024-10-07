import RPi.GPIO as gg
gg.setmode(gg.BCM)
gg.setup(24, gg.OUT)

p = gg.PWM(24, 50)
while True:
    t = int(input())
    p.start(t)
    input()
    p.stop
    gg.cleanup()