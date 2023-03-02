import numpy as np
import matplotlib.pyplot as plt

class SpikeData():
  
  def __init__(self, data_array, sample_rate):
    
    self.data_array = data_array
    self.sample_rate = sample_rate
    self.r_value = self.spike_count_rate()

  # spike-count rate (r) given spike data (organized by trial!)
  def spike_count_rate(self):
    return np.sum(self.data_array, axis=-1) / self.data_array.shape[-1]
  
  def visualize_spike_data(self):
    fig, axis = plt.subplots()
    axis.set_title(f"Neuronal Spike Time")
    axis.set_xlim([0, self.data_array.shape[-1]])
    axis.set_xlabel('Time (ms)')
    axis.set_yticks(range(self.data_array.shape[0]))
    axis.set_ylabel('Trial Number')

    for trial in range(self.data_array.shape[0]):
      axis.vlines([i for i, val in enumerate(self.data_array[trial,:]) if val == 1], trial - 0.5, trial + 0.5)
    plt.show()
  
  def __str__(self) -> str:
    return f"SPIKE DATA:\n{self.data_array}\nSpike Count Rate: {self.r_value}"
  
  def time_dependent_firing_rate(self, delta_t):
    if delta_t % self.sample_rate != 0:
      print("The sample rate is not divisible by Delta t!")
      return -1
    if len(self.data_array.shape) == 1:
      return self.r_value
    
    data = []
    inc = int(delta_t/self.sample_rate)
    print(f"Inc: {inc}")
    for i in range(0, self.data_array.shape[-1], inc):
      data.append(np.sum(np.sum(self.data_array[:, i:i+inc], axis=0)) / inc)
      
    print(data)