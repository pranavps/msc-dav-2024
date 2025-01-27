# titanic_all_data_steps_demo.py: This is a Python program that demonstrates how to preprocess and clean a dataset using the steps from the Titanic dataset.
# Author: Pranav Sahasrabudhe
# Email: pranav.sahasrabudhe@gmail.com
# (C)0 2024 - 2025 Pranav Sahasrabudhe)

# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("heptapod/titanic")

# print("Path to dataset files:", path)

# ================
import os

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Step 1: Load the dataset
# You need to download the dataset from Kaggle and place it in your working directory


# data_frame = pd.read_csv( r'C:\Users\prana\msc-dav-2024\data\Automobile_data.csv')
data_frame = pd.read_csv(os.path.join(os.path.dirname(__file__), '..\\data', 'titanic.csv'))



# Lets check the dropped data also
dropped_data = data_frame[data_frame.duplicated()]
print("--------------------------------------\n\n")
print("\nDropped Data:\n", dropped_data)
print("--------------------------------------\n\n")

# Step 2: Remove duplicates
data_frame = data_frame.drop_duplicates()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n")

print(data_frame)

# Step 3: Handle missing values
# For simplicity, we'll fill missing age values with the median age and drop rows with other missing values
# data_frame['Age'].fillna(data_frame['Age'].median(), inplace=True)
data_frame['Age'] = data_frame['Age'].fillna(data_frame['Age'].median())

data_frame = data_frame.dropna(subset=['Embarked', 'Fare'])  # Dropping rows with missing 'Embarked' and 'Fare' values
print("=========")
print(data_frame)

# Step 4: Correct errors
# In the Titanic dataset, there might not be blatant errors, but ensure correct data types
data_frame['Fare'] = pd.to_numeric(data_frame['Fare'], errors='coerce')
print("==== Fare Data Frame TO Numeric =====")
print(data_frame)

# Step 5: Normalize data
scaler = MinMaxScaler()
data_frame['Fare'] = scaler.fit_transform(data_frame[['Fare']])
print("==== Normalized Fare Data Frame =====")
print(data_frame)

data_frame['Age'] = scaler.fit_transform(data_frame[['Age']])
print("==== Normalized Age Data Frame =====")
print(data_frame)

<<<<<<< HEAD

#  Displaying the cleaned and prepared DataFrame1
# print(df.head())


=======
# Step 6: Transform and encode data
# Encoding 'Sex' and 'Embarked' columns
data_frame['Sex'] = data_frame['Sex'].map({'male': 1, 'female': 0})
data_frame = pd.get_dummies(data_frame, columns=['Embarked'])

# Displaying the cleaned and prepared DataFrame1
print(data_frame.head())
print("---------------")
print(data_frame.tail())
>>>>>>> 973bb1a07db2e215d20ecc1ef517b390ef6941b7
