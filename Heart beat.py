import numpy as np
import matplotlib.pyplot as plt
import time

# Function to scale the matrix
def gen(matr, val):
    return val * matr

# Time
t = np.linspace(0, 2 * np.pi, 1000)
timing = 60

# Heart equations
x = 16 * (np.sin(t))**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

xy = np.vstack((x, y))

# Scaling factors
scaling_factors1 = np.linspace(1, 2, timing)  # Scale up
scaling_factors2 = np.linspace(2, 1, timing)  # Scale down

# Create figure
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_title("Heart Beat Animation")
ax.grid(True)
ax.set_aspect('equal')


line, = ax.plot([], [], 'r', linewidth=2)

# Function to update plot
def update(scale):
    m = gen(xy, scale)
    line.set_data(m[0, :], m[1, :])
    plt.draw()
    plt.pause(1/timing)  # Pause 1/timing


while True:
    for scale in scaling_factors1:
        update(scale)
    for scale in scaling_factors2:
        update(scale)
