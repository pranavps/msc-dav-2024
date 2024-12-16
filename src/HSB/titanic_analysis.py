import kagglehub
import pandas as pd
import numpy as np

# Download latest version
path = kagglehub.dataset_download("heptapod/titanic")

print("Path to dataset files:", path)
data_frame=pd.read_csv('titanic.csv')
duplicates=data_frame[data_frame.duplicated()]
print(duplicates)
print(data_frame.drop_duplicates())
data_frame['Sex']=data_frame['Sex'].map(lambda x : "Male" if x == 0 else "Female")
print(data_frame)
data_frame['Age']=data_frame['Age'].fillna(data_frame['Age'].median())
data_frame=data_frame.dropna()
print(data_frame)
#code end
