import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data={'Age':[28,22,35,40,50,25,30,31,25,34,28]}
df=pd.DataFrame(data)
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Age')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
#calculating skewness and kurtosis
skewness = df['Age'].skew()
kurtosis = df['Age'].kurtosis()
print("Skewness: ", skewness)
print("Kurtosis", kurtosis)
