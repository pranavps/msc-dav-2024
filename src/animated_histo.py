import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Creating a figure and axis
fig, ax = plt.subplots()

# Function to update the histogram
def update_hist(num):
    ax.clear()
    data = np.random.randn(1000 + num*10)
    ax.hist(data, bins=30, alpha=0.7, color='blue')
    ax.set_title('Animated Histogram')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

# Creating the animation
ani = animation.FuncAnimation(fig, update_hist, frames=50, interval=100)

# Display the animation
plt.show()
