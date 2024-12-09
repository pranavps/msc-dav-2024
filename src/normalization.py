# The program to demonstrate how to normalize a DataFrame using the MinMaxScaler.
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, 22, 32]}

df = pd.DataFrame(data)

# Normalizing Age column
scaler = MinMaxScaler()
df['Age'] = scaler.fit_transform(df[['Age']])

print(df)
