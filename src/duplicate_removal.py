# The program to demonstrate how to remove duplicates from a DataFrame using the drop_duplicates function.
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'John', 'Mike'],
        'Age': [28, 22, 28, 32]}

df = pd.DataFrame(data)

#identifying duplicates
duplicates = df[df.duplicated(keep=False)]

# Removing duplicates
df_cleaned = df.drop_duplicates()

dropped_duplicates = duplicates[~duplicates.index.isin(df_cleaned.index)]
print(dropped_duplicates)

# print(duplicates)
# print(df_cleaned)
