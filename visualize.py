import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data from pipeline
df = pd.read_csv('lpbf_data_clean.csv')

# Create one figure with 3 subplots stacked vertically
fig, axes = plt.subplots(3, 1, figsize=(12, 10))
fig.suptitle('L-PBF Process Monitoring Dashboard', fontsize=14, fontweight='bold')

# Plot 1 - Melt pool temperature
axes[0].plot(df['layer'], df['melt_pool_temp'], 
             color='orange', linewidth=0.8, label='Temperature')
# Highlight spike locations in red
spikes = df[df['temp_spike_flag'] == True]
axes[0].scatter(spikes['layer'], spikes['melt_pool_temp'], 
                color='red', zorder=5, label='Spike detected', s=50)
axes[0].set_ylabel('Temperature (°C)')
axes[0].set_title('Melt Pool Temperature')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2 - Laser power
axes[1].plot(df['layer'], df['laser_power'], 
             color='blue', linewidth=0.8, label='Laser Power')
# Highlight dropout locations in red
dropouts = df[df['power_dropout_flag'] == True]
axes[1].scatter(dropouts['layer'], dropouts['laser_power'], 
                color='red', zorder=5, label='Dropout detected', s=50)
axes[1].set_ylabel('Power (W)')
axes[1].set_title('Laser Power')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Plot 3 - Layer density
axes[2].plot(df['layer'], df['layer_density'], 
             color='green', linewidth=0.8, label='Density (interpolated)')
axes[2].set_ylabel('Relative Density')
axes[2].set_xlabel('Layer Number')
axes[2].set_title('Layer Density Estimate')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('lpbf_monitoring_dashboard.png', dpi=150)
plt.show()
print("Dashboard saved as lpbf_monitoring_dashboard.png")