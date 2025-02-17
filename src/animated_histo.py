import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
data = pd.read_csv('C:/Users/Acer/msc-dav-2024/src/HSB/titanic.csv')
data = pd.DataFrame(data)
data = data['Age']
# Creating a figure and axis
fig, ax = plt.subplots()
data = pd.concat([data, data*2],ignore_index=True)



# Function to update the histogram
def update_hist(num):
    ax.clear()
    global data
    data = pd.concat([data, data*2],ignore_index=True)
    
    ax.hist(data, bins=30, alpha=0.7, color='blue')
    ax.set_title('Animated Histogram')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

# Creating the animation
ani = animation.FuncAnimation(fig, update_hist, frames=50, interval=100)

# Display the animation
plt.show()
