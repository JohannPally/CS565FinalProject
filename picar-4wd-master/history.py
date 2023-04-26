import numpy as np

class History:
    def __init__(self):
        self.positions = [np.array([50,50,200,201])]
        self.samples = [0.0]

    def add_position(self, detection):
        if detection is not None:
            self.positions.append(detection)
        else:
            print('no dog')
            self.positions.append(self.positions[-1])
        return

    def add_sample(self, sample):
        if sample is not None:
            self.samples.append(sample)
        else:
            self.samples.append(self.samples[-1])
        return
    
    #TODO check for alerts
    def check_noise(self):
        nse = np.abs(np.var(self.samples[len(self.samples) - min(10, len(self.samples)) : ])) 
        # > 10
        print('noise', nse)
        return np.abs(nse) > 100

    def check_spaz(self):
        sum = 0
        for i in range(1,min(len(self.positions)-1, 5)):
            j = i*-1
            # print(j)
            diff = np.subtract(self.positions[j], self.positions[j-1])
            s = np.sum(diff)
            sum += s
        print('movemnet', sum)
        # sum > 20
        return np.abs(sum) > 50
    
    #TODO plotting stuff
    def plot_positions(self):
        return

    def plot_samples(self):
        return