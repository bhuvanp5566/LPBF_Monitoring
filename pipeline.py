import numpy as np
import pandas as pd

# Load the CSV saved by data_generator.py
df = pd.read_csv('lpbf_data.csv')

# First quality check - understand what we're working with
print("=== RAW DATA INFO ===")
print(df.info())

# Second quality check - count missing values per column
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Step 1 - Temperature spike detection using 3-sigma rule
# Any value beyond mean + 3*std is almost certainly a fault
temp_mean = df['melt_pool_temp'].mean()
temp_std = df['melt_pool_temp'].std()
threshold = temp_mean + 3 * temp_std  # 99.7% of normal values fall below this

# Create new column - True if spike, False if normal
df['temp_spike_flag'] = df['melt_pool_temp'] > threshold

print("\n=== TEMPERATURE SPIKE DETECTION ===")
print(f"Mean: {temp_mean:.2f} | Std: {temp_std:.2f} | Threshold: {threshold:.2f}")
print(f"Spikes detected: {df['temp_spike_flag'].sum()}")

# Step 2 - Laser power dropout detection
# Dropout goes DOWN so we use less than threshold (mean - 3*std)
power_mean = df['laser_power'].mean()
power_std = df['laser_power'].std()
power_threshold = power_mean - 3 * power_std

# Create new column - True if dropout, False if normal
df['power_dropout_flag'] = df['laser_power'] < power_threshold

print("\n=== LASER POWER DROPOUT DETECTION ===")
print(f"Mean: {power_mean:.2f} | Std: {power_std:.2f} | Threshold: {power_threshold:.2f}")
print(f"Dropout layers detected: {df['power_dropout_flag'].sum()}")

# Step 3 - Handle missing density values
print("\n=== DENSITY MISSING VALUES ===")
print(f"Missing before: {df['layer_density'].isnull().sum()}")
df['layer_density'] = df['layer_density'].interpolate(method='linear')
print(f"Missing after: {df['layer_density'].isnull().sum()}")

# Step 4 - Save cleaned and flagged data
df.to_csv('lpbf_data_clean.csv', index=False)
print("\n=== PIPELINE COMPLETE ===")
print(f"Clean data saved to lpbf_data_clean.csv")
print(f"Total flagged layers: {df['temp_spike_flag'].sum() + df['power_dropout_flag'].sum()}")
print(df.head(10))