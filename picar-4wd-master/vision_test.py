from dog_detection import Vision

vis  = Vision()
for i in range(5):
    det = vis.check_dog()
    if det is not None:
        bb = det.bounding_box
        print(bb.origin_x, bb.origin_y, bb.width, bb.height)
    else:
        print('try again')
    input()