"""
================================================================================
Filename    : titanic_analysis.py
Author      : Harjas Singh Bajwa
Email       : hab2442007@sicsr.ac.in
Created     : 2024-12-16
Description : Doing analysis on Titanic Sample Dataset
--------------------------------------------------------------------------------
Usage       : <Specify usage or commands if applicable>
Dependencies: kaaglehub,pandas,numpy
--------------------------------------------------------------------------------
Version History:
    2024-12-17 - Version 1.0 - Initial version.
--------------------------------------------------------------------------------
License     : Na
================================================================================
"""



import kagglehub
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Download latest version
path = kagglehub.dataset_download("heptapod/titanic")
scaler=MinMaxScaler()
print("Path to dataset files:", path)
data_frame=pd.read_csv('titanic.csv')
duplicates=data_frame[data_frame.duplicated()]
print("Duplicates Values")
print(duplicates)
print("Removing Duplicates")
print(data_frame.drop_duplicates())
data_frame=data_frame.drop_duplicates()
data_frame[["Fare","Age"]]=scaler.fit_transform(data_frame[['Fare','Age']])
data_frame['Sex']=data_frame['Sex'].map(lambda x : "Male" if x == 0 else "Female")
print(data_frame)
data_frame['Age']=data_frame['Age'].fillna(data_frame['Age'].median())
data_frame=data_frame.dropna()
print("Data Frame after removing null")
print(data_frame.head())
print("embarked dataset")
data_frame=pd.get_dummies(data_frame,columns=['Embarked'])
print(data_frame.head())


#code end
