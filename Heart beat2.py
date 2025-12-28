import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from numpy.ma.core import sqrt

# Initial value of k
k_init = 100

# Data domain
x = np.linspace(-3, 3, 10000)

def heart_curve(x, k):
    return abs(x)**(2/3) + 0.9 * np.sin(k * x) * sqrt(3 - x * x)

# Initial plot
y = heart_curve(x, k_init)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

line, = ax.plot(x, y)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal', adjustable='box')

# Slider axis
ax_k = plt.axes([0.15, 0.1, 0.7, 0.03])
k_slider = Slider(
    ax=ax_k,
    label='k',
    valmin=1,
    valmax=150,
    valinit=k_init,
    valstep=1
)

# Update function
def update(val):
    k = k_slider.val
    line.set_ydata(heart_curve(x, k))
    fig.canvas.draw_idle()

k_slider.on_changed(update)

plt.show()

if __name__ == "__main__":
    pass
