# The program to demonstrate how to correct errors in a DataFrame using the to_numeric function.
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, 22, 'ThirtyTwo']}

df = pd.DataFrame(data)

# Correcting the error in Age
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

print(df)
