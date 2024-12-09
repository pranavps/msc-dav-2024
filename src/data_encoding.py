# The program to demonstrate how to encode categorical data using label encoding.
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Gender': ['Male', 'Female', 'Male']}

df = pd.DataFrame(data)

# Encoding Gender column
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

print(df)
