import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data={'Age':[28,22,35,40,50,30,31,25,34,28],'Price':[1000,800,1200,1500,2000,1100,700,1300,1000,1200]}
df=pd.DataFrame(data)

plt.scatter(df['Age'],df['Price'])
plt.xlabel("Age")
plt.ylabel("Price")
plt.show()

coefficients=np.polyfit(df['Age'],df['Price'],1)
intercept=coefficients[1]
slope=coefficients[0]
print(f"Linear Regression: y = {slope}x + {intercept}")
x=np.linspace(df['Age'].min(), df['Age'].max(),100)
y=slope * x + intercept
plt.plot(x,y,color='red')
plt.show()

