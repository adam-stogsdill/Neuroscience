import numpy as np
import dirac_delta as dd
from spike_data import SpikeData

def create_spike_data(length=10):
  spike_data = np.random.rand(length)
  return (spike_data >= .5).astype(np.int8)

data_list = []
for i in range(20):
  data_list.append(create_spike_data(100))
data = np.asarray(data_list)
example_data = SpikeData(data, 0.001)
print(example_data)
#print(np.sum(np.sum(example_data.data_array[:, 0:2], axis=0)))
example_data.visualize_spike_data()
example_data.time_dependent_firing_rate(0.002)