import picar_4wd as fc
import numpy as np
import matplotlib.pyplot as plt
import time

#TODO change to just turning a wheel
class Dispense:

    def __init__(self):
        fc.stop()
        self.treats = 0

        return
    
    def check_message(self, mess):
        print()
        print(mess)
        print(type(mess))
        return b'good job!' == mess
    
    def act(self, mess):
        if self.check_message(mess):
            print('good job detected')
            #TODO drop a treat
            fc.forward(10)
            time.sleep(.5)
            fc.stop()
            self.treats += 1
            return self.treats
        
        else:
            print('not good job')
            return None