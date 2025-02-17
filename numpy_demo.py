import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
data = np.random.rand(4, 4)  # Generating random data for demonstration
print(data)
# Calculate correlation matrix
correlation_matrix = np.corrcoef(data)
print(correlation_matrix)
# Create a heatmap
sns.heatmap(correlation_matrix, annot=True)
plt.show()
