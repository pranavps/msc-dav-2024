import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data={'values': [28,22,25,40,50,30,31,25,34,28]}
df = pd.DataFrame(data)
range_val=df['values'].max() - df['values'].min()
iqr=df['values'].quantile(0.75) - df['values'].quantile(0.25)
varience=df['values'].var()
std_dev=df['values'].std()
mean=np.mean(df['values'])
print(f"Range : {range_val}, IQR : {iqr} Standard deviation : {std_dev} Var :{varience} Mean : {mean}")
#box plot
df.boxplot(column='values')
plt.title('Box Plot of Values')
plt.show()