from dog_detection import Vision
import time

vis = Vision()

while True:
    print('seeing...')
    print(vis.check_dog())
    print('sleeping...')
    time.sleep(1)