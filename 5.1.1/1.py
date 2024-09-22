import matplotlib.pyplot as plt
import numpy as np

# Data
wave = [7032, 6929, 6717, 6678, 6599, 6533, 6507, 6402, 6383, 6334, 6305, 6267, 6217, 6164, 6143, 6096, 6030, 5976, 5882, 5852, 5401, 5341, 5331]
deg  = [2566, 2498, 2488, 2464, 2428, 2392, 2384, 2364, 2352, 2336, 2316, 2292, 2284, 2264, 2254, 2234, 2204, 2194, 2164, 2148, 2102, 1882, 1838]

# Calculate error values
x_err = np.array(deg) * 0.01  # 3% error on x-axis
y_err = np.array(wave) * 0.02  # 7.5% error on y-axis

# Polynomial fit (degree 2)
t = np.polyfit(deg, wave, 2)
f = np.poly1d(t)

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

# Plot the experimental data without markers
ax.errorbar(deg, wave, xerr=x_err, yerr=y_err, fmt='o', color='b', label='Эксперименты', capsize=5)

# Plot the polynomial fit
deg_fit = np.linspace(min(deg), max(deg), 500)
ax.plot(deg_fit, f(deg_fit), linestyle="-", marker='None', color='r', label='Аппроксимация')

# Axis labels
ax.set_xlabel(r'θ, °', fontsize=12.5)
ax.set_ylabel(r'λ, Å', fontsize=12.5)

# Axis ticks and grid
ax.xaxis.set_minor_locator(plt.MultipleLocator(50)) 
ax.yaxis.set_minor_locator(plt.MultipleLocator(100))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=5)

ax.grid(which='major', linestyle='-') 
ax.grid(which='minor', linestyle='--')
equation_text = r'$V1 = {:.2f}x^2 + {:.2f}x + {:.2f}$'.format(t[0], t[1], t[2])
ax.text(0.95, 0.05, equation_text, fontsize=8, color='black', ha='right', va='bottom', transform=ax.transAxes)

# Add legend
ax.legend(fontsize=12.5)

# Show and save the plot
plt.show()
fig.savefig("Градуировка_монохроматора.png")
