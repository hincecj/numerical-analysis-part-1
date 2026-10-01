import numpy as np
import matplotlib.pyplot as plt

# Initial parameters
G = 1.0 # gravitational constant
h = 0.01 # time step
n = 1000 # iterations
a = 2 # plot boundaries

# Masses
m1 = 1.0
m2 = 1.0
m3 = 1.0

# Initial positions
x1 = np.array([0.0, 0.57735])
x2 = np.array([-0.5, -0.28868])
x3 = np.array([0.5, -0.28868])

# Initial velocities
v1 = np.array([-1.0, 0.0])
v2 = np.array([0.5, -0.86603])
v3 = np.array([0.5, 0.86603])



# FIGURE EIGHT
# x1 = np.array([-0.97004, 0.24309])
# x2 = np.array([0.97004, -0.24309])
# x3 = np.array([0.0, 0.0])

# v1 = np.array([0.46620, 0.43237])
# v2 = np.array([0.46620, 0.43237])
# v3 = np.array([-0.93240, -0.86473])



# IN LINE
# x1 = np.array([-1.0, 0.0])
# x2 = np.array([0.0, 0.0])
# x3 = np.array([1.0, 0.0])

# v1 = np.array([0.0, 0.5])
# v2 = np.array([0.0, 0.0])
# v3 = np.array([0.0, -0.5])



# SUN EARTH MARS
# m1 = 100.0
# m2 = 1.0
# m3 = 1.0

# x1 = np.array([0.0, 0.0])
# x2 = np.array([0.65617, 0.0])
# x3 = np.array([-1.0, 0.0])

# v1 = np.array([0.0, 0.0])
# v2 = np.array([0.0, 12.347])
# v3 = np.array([0.0, -10.0])



# Second positions using Taylor series
y1 = x1 + h * v1 + h**2 / 2 * G * (m2 * (x2 - x1) / np.linalg.norm(x2 - x1) ** 3 + m3 * (x3 - x1) / np.linalg.norm(x3 - x1) ** 3)
y2 = x2 + h * v2 + h**2 / 2 * G * (m1 * (x1 - x2) / np.linalg.norm(x1 - x2) ** 3 + m3 * (x3 - x2) / np.linalg.norm(x3 - x2) ** 3)
y3 = x3 + h * v3 + h**2 / 2 * G * (m1 * (x1 - x3) / np.linalg.norm(x1 - x3) ** 3 + m2 * (x2 - x3) / np.linalg.norm(x2 - x3) ** 3)

# Store previous position for recursion as [previous, current]
x1 = np.vstack([x1, y1])
x2 = np.vstack([x2, y2])
x3 = np.vstack([x3, y3])

# Initialise plot
plt.style.use("dark_background")
plt.ion()
fig, ax = plt.subplots(figsize = (8, 8))

# Integration algorithm and plotting
for i in range(n):
    # Recursive integration algorithm
    x1n = h ** 2 * G * (m2 * (x2[1] - x1[1]) / np.linalg.norm(x2[1] - x1[1]) ** 3 + m3 * (x3[1] - x1[1]) / np.linalg.norm(x3[1] - x1[1]) ** 3) + 2 * x1[1] - x1[0]
    x2n = h ** 2 * G * (m1 * (x1[1] - x2[1]) / np.linalg.norm(x1[1] - x2[1]) ** 3 + m3 * (x3[1] - x2[1]) / np.linalg.norm(x3[1] - x2[1]) ** 3) + 2 * x2[1] - x2[0]
    x3n = h ** 2 * G * (m1 * (x1[1] - x3[1]) / np.linalg.norm(x1[1] - x3[1]) ** 3 + m2 * (x2[1] - x3[1]) / np.linalg.norm(x2[1] - x3[1]) ** 3) + 2 * x3[1] - x3[0]

    # Current stored as previous, new stored as current
    x1[0] = x1[1]
    x1[1] = x1n

    x2[0] = x2[1]
    x2[1] = x2n

    x3[0] = x3[1]
    x3[1] = x3n

    # Plotting
    ax.clear()

    ax.scatter(*x1[1], color = 'white', s = 50 * m1)
    ax.scatter(*x2[1], color = 'white', s = 50 * m2)
    ax.scatter(*x3[1], color = 'white', s = 50 * m3)

    ax.set_xlim(-a, a)
    ax.set_ylim(-a, a)
    ax.set_aspect('equal')
    ax.tick_params(left = False, bottom = False, labelleft = False, labelbottom = False)

    plt.pause(h)

    if not plt.fignum_exists(fig.number):
        break

plt.ioff()
plt.show()
