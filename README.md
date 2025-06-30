# ❤️ Heartbeat Animation using Matplotlib

This project creates a simple, visually appealing heartbeat animation using Python's `matplotlib` and `numpy` libraries. The animation simulates the pulsing of a heart by dynamically scaling a parametric heart curve.

## 📽️ Demo
The animation continuously scales a heart shape up and down, simulating a heartbeat. It uses parametric equations and real-time updates with `matplotlib`.

## 🧠 How It Works

The heart shape is defined using parametric equations:

$$
\begin{align*}
x &= 16 \sin^3(t) \\
y &= 13\cos(t) - 5\cos(2t) - 2\cos(3t) - \cos(4t)
\end{align*}
$$


