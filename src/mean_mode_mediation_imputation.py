# The program to demonstrate how to impute missing values in a DataFrame using the mean, mode, and median methods.
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, None, 32]}

df = pd.DataFrame(data)

# Imputing missing values with median
df['Age'].fillna(df['Age'].median(), inplace=True)

print(df)
