from dog_detection import Vision

vis = Vision()

while True:
    dc = vis.check_dog() 
    if dc is not None:
        print(dc)