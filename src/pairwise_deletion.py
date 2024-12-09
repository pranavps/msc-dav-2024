# The program to demonstrate how to perform pairwise deletion in a DataFrame using the dropna function.
import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Anna', 'Mike'],
        'Age': [28, None, 32],
        'Score': [85, 90, None]}

df = pd.DataFrame(data)

# Performing calculations ignoring missing values
mean_age = df['Age'].mean()
mean_score = df['Score'].mean()

print(f'Mean Age: {mean_age}, Mean Score: {mean_score}')
