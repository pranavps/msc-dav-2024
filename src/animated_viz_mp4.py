import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

# Saving the animation as a video
writer = animation.FFMpegWriter(fps=20)
ani.save("sine_wave.mp4", writer=writer)

print("Animation saved as sine_wave.mp4")
