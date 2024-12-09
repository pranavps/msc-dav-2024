# The program to demonstrate how to scale a DataFrame using the StandardScaler.
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, 22, 32]}

df = pd.DataFrame(data)

# Scaling Age column
# Create an instance of the StandardScaler
# This will be used to scale the values in the 'Age' column
# The StandardScaler is a class from scikit-learn that is used to standardize features by removing the mean and scaling to unit variance

# What StandardScaler Does
# StandardScaler standardizes features by removing the mean and scaling to unit variance. This means it will transform your data such that the resulting distribution has a mean of 0 and a standard deviation of 1.

# Why Use StandardScaler?
# Standardizing data is a common preprocessing step because:

# Consistency: It ensures that all features contribute equally to the model by putting them on a common scale.

# Performance: Some algorithms (like gradient descent) converge faster when features are standardized.
scaler = StandardScaler()
df['Age'] = scaler.fit_transform(df[['Age']])

print(df)
