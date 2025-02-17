from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Creating a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 128)
line, = ax.plot(x, np.sin(x))

# Animation function
def animate(i):
    line.set_ydata(np.sin(x + i / 10))
    return line,

# Creating the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.show()

# ------------------------------
from matplotlib.animation import PillowWriter

# Saving the animation as a GIF
writer = PillowWriter(fps=20)
ani.save("sine_wave.gif", writer=writer)

# ------------------------------
# Saving the animation as a video
writer = animation.FFMpegWriter(fps=20)
# ani.save("sine_wave.mp4", writer=writer)

# ------------------------------