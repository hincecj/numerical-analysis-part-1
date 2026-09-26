import numpy as np
import matplotlib.pyplot as plt

# Initial parameters
g = 9.81 # gravitational constant
h = 0.03 # time step
n = 1000 # iterations

# Initial conditions
l = 1.0 # rod length
a0 = 3 # initial angle
m = 1.0 # mass
mu = 0.2 # drag coefficient

# Calculate a1
a1 = a0 - (h ** 2 * g) / (2 * l) * np.sin(a0)

# Store previous angles for recursion
a = np.array([a0, a1])

# Initialise plot
plt.style.use("dark_background")
plt.ion()
fig, ax = plt.subplots(figsize = (8, 8))

for i in range(n):
    # Recursive integration for a
    anew = (2 * m * l * (2 * l * a[1] - h ** 2 * g * np.sin(a[1])) + (h * mu - 2 * m * l ** 2) * a[0]) / (h * mu + 2 * m * l ** 2)

    # Current stored as previous, new stored as current
    a[0] = a[1]
    a[1] = anew

    # Convert to x, y coordinates for plotting
    x = l * np.sin(a[1])
    y = -l * np.cos(a[1])

    # Plotting
    ax.clear()

    ax.scatter(0, 0, color = 'white')
    ax.scatter(x, y, color = 'white', s = 200)
    ax.plot([0, x],[0, y], color = 'white')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.tick_params(left = False, bottom = False, labelleft = False, labelbottom = False)
    ax.set_title(f"t = {i*h:.2f} s")
    
    plt.pause(h)
    
    if not plt.fignum_exists(fig.number):
        break

plt.ioff()
plt.show()