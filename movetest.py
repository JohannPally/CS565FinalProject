import picar_4wd as fc
import time

while True:
    fc.forward(20)
    time.sleep(1)
    fc.stop()
    time.sleep(1)

