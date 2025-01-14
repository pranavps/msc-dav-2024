import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = {'Age':[28,22,35,40,50,30,31,25,34,28]}
df = pd.DataFrame(data)

#Descriptive Statistics
mean = df['Age'].mean()
median = df['Age'].median()
mode = df['Age'].mode()[0]

print(f'Mean: {mean}, Median: {median}, Mode: {mode}')

#Confidence Interval
confidence_level = 0.95
degree_freedom = len(df['Age']) - 1
sample_mean = np.mean(df['Age'])
sample_standard_error = np.std(df['Age'], ddof=1) / np.sqrt(len(df['Age']))
confidence_interval = np.percentile(
    sample_mean + sample_standard_error * np.array([-1.96 , 1.96]), [2.5, 97.5]
)

print(f'95% Confidence Interval: {confidence_interval}')