from history import History
import numpy as np

h = History()

h.add_position(np.array([0,0,0,0]))
h.add_position(np.array([50,70,0,0]))
h.add_position(np.array([30,0,0,0]))
h.add_position(np.array([10,0,0,0]))
print(h.check_spaz())
print(h.positions)

h.add_position(np.array([0,0,0,0]))
h.add_position(np.array([0,0,0,0]))
print(h.positions)
h.add_position(None)
print(h.positions)
h.add_position(np.array([0,0,0,0]))
print(h.positions)
