
class History:
    def __init__(self):
        self.positions = []
        self.samples = []

    def add_position(self, detection):
        if detection is not None:
            #TODO check how to get position from detection
            self.positions.append((0,0))
        else:
            self.positions.append(self.positions[-1])
        return

    def add_sample(self, sample):
        if sample is not None:
            self.samples.append(sample)
        else:
            self.samples.append(self.samples[-1])
        return
    
    #TODO plotting stuff
    def plot_positions(self):
        return

    def plot_samples(self):
        return