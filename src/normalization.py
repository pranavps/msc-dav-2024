# The program to demonstrate how to normalize a DataFrame using the MinMaxScaler.
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, 22, 32]}

df = pd.DataFrame(data)

# Now explain me thi: # Normalizing Age column scaler = MinMaxScaler() df['Age'] = scaler.fit_transform(df[['Age']])
# Normalizing the Age Column
# MinMaxScaler: This is a tool from scikit-learn that transforms features by scaling each feature to a given range, usually between 0 and 1. It ensures that all values fit within this range, making data easier to compare.
# Initializing the Scaler: scaler = MinMaxScaler()
# Here, we're creating an instance of MinMaxScaler.
# Fitting and Transforming the Data: df['Age'] = scaler.fit_transform(df[['Age']])
# Fitting: When we call fit_transform(), the scaler first calculates the minimum and maximum values from the 'Age' column.
# Transforming: It then scales all the values in the 'Age' column to the range [0, 1].
# Example
#  Suppose the 'Age' column originally has values: [20, 30, 40, 50]
# Minimum Age: 20
# Maximum Age: 50
# For each value 

# Normalizing Age column
scaler = MinMaxScaler()
df['Age'] = scaler.fit_transform(df[['Age']])

print(df)
