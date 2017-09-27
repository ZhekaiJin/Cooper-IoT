from picamera import PiCamera
from time import sleep

# various of camera setup/attributes
camera = PiCamera()
# camera.rotation = 180
# camera.resolution = (1920,1080)
# camera.framerate = 15
# camera.brightness = 70
# camera.annotate_text_size = 50




camera.start_preview()
# camera.start_recording('test.h264')
sleep(10)
# camera.capture('test.jpg')
# camera.stop_recording()
camera.stop_preview()
