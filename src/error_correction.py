# The program to demonstrate how to correct errors in a DataFrame using the to_numeric function.
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, 22, 'ThirtyTwo']}

df = pd.DataFrame(data)

# Correcting the error in Age
'''The code is doing exactly what it's designed to do. When you use pd.to_numeric() with errors='coerce', 
it converts invalid entries (like "Thirty Two") to NaN (Not a Number) because it can't interpret 
"ThirtyTwo" as a numeric value.
If you want to replace NaN values with a specific numeric value, you can use the fillna() method. 
For example, if you want to replace NaN with 0, you can use df['Age'].fillna(0).'''

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

print(df)
# val = int('ThirtyTwo')
# print("Converting string to numeric: Thirty Two: {}")
