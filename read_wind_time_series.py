import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# Write Vortex Time series
df = pd.read_csv('vortex.serie.txt', header=2, delim_whitespace=True)

# Extract wind direction and wind speed columns
directions = df['direction']
speeds = df['speed']

# Plot wind rose
ax = WindroseAxes.from_ax()
ax.bar(directions, speeds, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.title('Wind Rose')

# Plot Weibull histogram
plt.figure()
plt.hist(speeds, bins=30, density=True)
plt.title('Weibull Histogram')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Probability Density')

plt.show()

