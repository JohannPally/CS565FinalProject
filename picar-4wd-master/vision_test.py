from dog_detection import Vision

vis  = Vision()
for i in range(5):
    det = vis.check_dog()
    bb = det.bounding_box
    print(bb.origin_x, bb.origin_y, bb.width, bb.height)
    
    input()