from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
camera.annotate_text = 'Hello world!'
#time.sleep(2)
# Take a picture including the annotation
#camera.capture('foo.jpg')
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')
camera.capture('foo1.jpg', resize=(320, 240))
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
camera.wait_recording(60)
camera.stop_recording()