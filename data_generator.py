import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

n_layers = 200
layers = np.arange(1, n_layers+1) #np.arange(start, stop)
time = np.linspace(0, 100, n_layers) #np.linspace(start, stop, num_points)

# Signal 1 - Melt pool temperatures
melt_pool_temp = np.random.normal(1500, 20, n_layers) #np.random.normal(mean, std_dev, num_points)
spike_indicies = np.random.choice(n_layers, 5, replace=False) #np.random.choice(array_size, size, replace) 
melt_pool_temp[spike_indicies] += 200 # Add spikes to the melt pool temperature

# Signal 2 - Layer height deviations