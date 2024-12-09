# The program to demonstrate how to remove rows with missing values from a DataFrame using the dropna function.
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, None, 32]}

df = pd.DataFrame(data)

# Removing rows with missing values
df = df.dropna()

print(df)
