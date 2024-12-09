# The program to demonstrate how to merge two DataFrames using the merge function.
import pandas as pd

# Sample DataFrames
data1 = {'ID': [1, 2], 'Name': ['John', 'Anna']}
data2 = {'ID': [2, 3], 'Name': ['Anna', 'Mike']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merging DataFrames
df = pd.merge(df1, df2, on='ID', how='outer')

print(df)
