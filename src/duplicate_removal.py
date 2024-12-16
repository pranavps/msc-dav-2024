# The program to demonstrate how to remove duplicates from a DataFrame using the drop_duplicates function.
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'John', 'Mike'],
        'Age': [28, 22, 28, 32]}

df = pd.DataFrame(data)

# Removing duplicates
df = df.drop_duplicates()

print(df)
