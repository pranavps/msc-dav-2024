# The program to demonstrate how to fill missing values in a DataFrame using the mean method.
# Imputation: Filling missing values with mean
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, None, 32]}

df = pd.DataFrame(data)

# Filling missing values with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)

print(df)
