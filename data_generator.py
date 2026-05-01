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

# Signal 2 - Laser power
laser_power = np.random.normal(200, 2, n_layers)
laser_power[80:90] = 10 # Simulate a power drop between layers 80 and 90

# Signal 3 - Layer density estimate
layer_density = 0.99 - 0.001 * np.exp(-layers / 50) + np.random.normal(0, 0.005, n_layers) # Simulate a gradual increase in density with some noise
missing_indices = np.random.choice(n_layers, 10, replace=False)
layer_density[missing_indices] = np.nan


# Create DataFrame
df = pd.DataFrame({
    'layer': layers,
    'time': time,             # column name : data array
    'melt_pool_temp': melt_pool_temp,
    'laser_power': laser_power,
    'layer_density': layer_density
})

df.to_csv('lpbf_data.csv', index=False)
print("Data generated and saved to lpbf_data.csv")
print(df.head())