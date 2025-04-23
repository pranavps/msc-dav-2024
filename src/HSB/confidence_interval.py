import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data={'Age':[28,22,35,40,50,30,31,25,34,28]}
df=pd.DataFrame(data)
mean=df['Age'].mean()
median=df['Age'].median()
mode=df['Age'].mode()[0]

print(f"Mean :{mean}, Median:{median}, Mode:{mode}")
confidence_level=0.05
degrees_freedom=len(df['Age'])-1
sample_standard_error=np.std(df['Age'], ddof=1)/np.sqrt(len(df['Age']))
confidence_interval=np.percentile(mean + sample_standard_error * np.array([-1.96,1.96]),[2.5,97.5])
print(f"95% confidence interval: {confidence_interval}")