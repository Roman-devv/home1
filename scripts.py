from picamera import PiCamera 
import time

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
time.sleep(10)
camera.capture('blue.jpg')
