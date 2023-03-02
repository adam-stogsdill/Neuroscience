import numpy as np

# spike-count rate (r) given n_spikes
def spike_count_rate(n_spikes, period_length):
  return n_spikes / period_length

# spike-count rate (r) given spike data
def spike_count_rate(spike_data):
  return np.sum(spike_data, axis=-1) / np.shape[-1]