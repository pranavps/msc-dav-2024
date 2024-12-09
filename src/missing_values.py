# 
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, None, 32]}

df = pd.DataFrame(data)

# Removing rows with missing values
df = df.dropna()

print(df)
