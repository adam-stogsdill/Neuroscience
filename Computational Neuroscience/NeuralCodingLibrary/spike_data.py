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
  
  def visualize_spike_data(self, delta_t=10, trial=0):
    fig, axis = plt.subplots(5, 1)
    axis[0].set_title(f"Neuronal Spike Time")
    axis[0].set_xlim([0, self.data_array.shape[-1]])
    axis[0].set_xlabel('Time (ms)')
    axis[0].set_yticks(range(self.data_array.shape[0]))
    axis[0].set_ylabel('Trial Number')

    axis[0].vlines([i for i, val in enumerate(self.data_array[trial,:]) if val == 1], 0, 1)
    
    # Try Binning
    #axis[1].set_yticks([50, 100])
    axis[1].set_xlim([0, self.data_array.shape[-1]])
    delta_t = 0.1
    bin_values = self.time_dependent_firing_rate(delta_t=delta_t)
    values = []
    for i in range(len(bin_values)):
      values.extend([bin_values[i]] * int(delta_t/self.sample_rate))
    #print("VALUES:", values, len(values))
    axis[1].plot([i for i in range(len(values))], values)
    
    # Sliding window function
    window_bin_values = []
    axis[2].set_xlim([0, self.data_array.shape[-1]])
    
    t_i_values = np.where(self.data_array)[1]
    for t in range(0, self.data_array.shape[-1]):
      summation = 0
      for t_i in range(0, t_i_values.shape[-1]):
        parameter = t - t_i_values[t_i]
        if (-delta_t*1000 / 2 <= parameter < delta_t*1000 / 2): # Multiply by 1000 to get to MS instead of seconds
          summation += 1/delta_t
        else:
          continue 
      window_bin_values.append(summation)
    axis[2].plot([i for i in range(len(values))], window_bin_values)
    
    # Gaussian Window
    window_bin_values = []
    sigma_w = 10
    axis[3].set_xlim([0, self.data_array.shape[-1]])
    
    t_i_values = np.where(self.data_array)[1]
    for t in range(0, self.data_array.shape[-1]):
      summation = 0
      for t_i in range(0, t_i_values.shape[-1]):
        tau = t - t_i_values[t_i]
        a = 1 / (np.sqrt(2*np.pi) * sigma_w)
        b = np.exp(-1*(tau**2)/(2*(sigma_w**2)))
        summation += a*b
      window_bin_values.append(summation)
    #print("WINDOW:", window_bin_values)
    axis[3].plot([i for i in range(len(values))], window_bin_values)
    
    # Alpha-Window
    window_bin_values = []
    alpha = 0.1
    axis[4].set_xlim([0, self.data_array.shape[-1]])
    
    t_i_values = np.where(self.data_array)[1]
    for t in range(0, self.data_array.shape[-1]):
      summation = 0
      for t_i in range(0, t_i_values.shape[-1]):
        tau = t - t_i_values[t_i]
        val = (alpha ** 2) * tau * np.exp(-alpha*tau)
        if val >= 0:
          summation += val
        else:
          summation += 0
      window_bin_values.append(summation)
    print("WINDOW:", window_bin_values)
    axis[4].plot([i for i in range(len(values))], window_bin_values)
    
    plt.show()
    
    
  
  def __str__(self) -> str:
    return f"SPIKE DATA:\n{self.data_array}\nSpike Count Rate: {self.r_value}"
  
  def time_dependent_firing_rate(self, delta_t):
    if len(self.data_array.shape) == 1:
      return self.r_value
    
    data = []
    inc = int(delta_t/self.sample_rate)
    print(f"Inc: {inc}")
    for i in range(0, self.data_array.shape[-1], inc):
      data.append(np.sum(np.sum(self.data_array[:, i:i+inc], axis=0)) / delta_t)
    
    return data