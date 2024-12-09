# The program to demonstrate how to scale a DataFrame using the StandardScaler.
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, 22, 32]}

df = pd.DataFrame(data)

# Scaling Age column
scaler = StandardScaler()
df['Age'] = scaler.fit_transform(df[['Age']])

print(df)
