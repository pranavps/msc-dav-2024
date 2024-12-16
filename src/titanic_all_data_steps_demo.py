# The program to demonstrate how to preprocess and clean a dataset using the steps from the Titanic dataset.
# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("heptapod/titanic")

# print("Path to dataset files:", path)
# ================
import pandas as pd
# from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Step 1: Load the dataset
# You need to download the dataset from Kaggle and place it in your working directory
df = pd.read_csv(r'.\data\titanic.csv')

#dropped data
duplicates = df[df.duplicated()]
print(duplicates)
# Step 2: Remove duplicates
df = df.drop_duplicates()

# Step 3: Handle missing values
# For simplicity, we'll fill missing age values with the median age and drop rows with other missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df = df.dropna(subset=['Embarked', 'Fare'])  # Dropping rows with missing 'Embarked' and 'Fare' values

# Step 4: Correct errors
# In the Titanic dataset, there might not be blatant errors, but ensure correct data types
df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce')

# Step 5: Normalize data
# scaler = MinMaxScaler()
# df['Fare'] = scaler.fit_transform(df[['Fare']])

# Step 6: Transform and encode data
# Encoding 'Sex' and 'Embarked' columns
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
df = pd.get_dummies(df, columns=['Embarked'])
 
# Displaying the cleaned and prepared DataFrame
print(df.head())
