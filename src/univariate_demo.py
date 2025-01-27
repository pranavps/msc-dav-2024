import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Values': [28, 22, 35, 40, 50, 30, 31, 25, 34, 28]}
df = pd.DataFrame(data)

# Calculating Spread
range_val = df['Values'].max() - df['Values'].min()
iqr = df['Values'].quantile(0.75) - df['Values'].quantile(0.25)
variance = df['Values'].var()
std_dev = df['Values'].std()
mean = np.mean(df['Values'])

print(f'Range: {range_val}, IQR: {iqr}, Variance: {
      variance}, Standard Deviation: {std_dev}' f'Mean: {mean}')

# Box Plot
df.boxplot(column='Values')
plt.title('Box Plot of Values')
plt.show()
