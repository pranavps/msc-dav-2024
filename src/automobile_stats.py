# The program to demonstrate basic statistics calculations like mean, median, mode, standard deviation, variance, etc.
# from Automobile_data.csv dataset from Kaggle.
# (C) 2024 Pranav Sahasrabudhe

import pandas as pd # for data manipulation
import numpy as np # for mathematical operations
import matplotlib.pyplot as plt # for visualization
import seaborn as sns # for visualization

csv_path = r"C:\Users\prana\msc-dav\data"
# Load the dataset
auto_data = pd.read_csv(csv_path + r"\Automobile_data.csv")

# Basic summary statistics
print(auto_data.describe())

# Calculate variance for a specific column (e.g., engine size)
variance_engine_size = np.var(auto_data['engine-size'], ddof=1)

# Visualize the distribution of a specific column (e.g., price)
# Create a new figure with a specified size
# Create a new figure for the plot with a specified size
plt.figure(figsize=(10, 6))

# Plot a histogram of the 'price' column from the dataset
# 'bins=30' specifies the number of bins in the histogram
# 'kde=True' adds a Kernel Density Estimate to the plot
# 'color='blue'' sets the color of the bars to blue
sns.histplot(auto_data['price'], bins=30, kde=True, color='blue')

# Add a title to the plot
plt.title('Distribution of Automobile Prices')

# Label the x-axis
plt.xlabel('Price')

# Label the y-axis
plt.ylabel('Count')

# Display the plot
plt.show()

# Print variance
print(variance_engine_size)
