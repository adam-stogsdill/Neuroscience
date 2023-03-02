import numpy
from enum import Enum


# Neural Response Function

class RULE(Enum):
  midpoint = 0
  left = 1
  right = 2

# spike-count rate (r)
def spike_count_rate(n_spikes, period_length):
  return n_spikes / period_length

def spike_count_rate_by_function(func, period_length, delta_tau=0.01, rule=RULE.midpoint):
  sum = 0
  
  # Allow this function to approximate the integral of the function using Reimann sums!
  for i in range(0, period_length+1, period_length/delta_tau):
    if rule == RULE.midpoint:
      midpoint_value = (i + period_length/delta_tau) / 2
      sum += func(midpoint_value)
    elif rule == RULE.left:
      sum += func(i)
    elif rule == RULE.right:
      right_value = i + period_length/delta_tau
      sum += func(right_value)
  return sum