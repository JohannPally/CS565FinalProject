from dog_detection import Vision

vis  = Vision()
for i in range(5):
    print(vis.check_dog())
    input()