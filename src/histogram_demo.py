import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Age': [28, 22, 35, 40, 50, 30, 31, 25, 34, 28]}
df = pd.DataFrame(data)

# Plotting histogram
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Calculating Skewness and Kurtosis
skewness = df['Age'].skew()
kurtosis = df['Age'].kurt()
print(f'Skewness: {skewness}, Kurtosis: {kurtosis}')
