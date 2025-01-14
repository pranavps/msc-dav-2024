import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import streamlit as st

data = pd.read_csv(r"C:\Users\Abhiyanshu\Downloads\pre-owned cars.csv")
original_data = pd.read_csv(r"C:\Users\Abhiyanshu\Downloads\archive (6)\pre-owned cars.csv")

#displaying all rows
pd.set_option('display.max_columns',None)
#displaying float number upto 2 decimal
pd.set_option('display.float_format', '{:.2f}'.format)

st.title('Pre-Owned cars Data Processing')

#download button for original dataset
st.download_button(
    label="Download Original Dataset",
    data=original_data.to_csv(index=False).encode('utf-8'),
    file_name='pre-owned_cars_original.csv',
    mime='text/csv'
)
#printing the dataset
st.header("Summary statistics")
# print(data)
st.write(data.info())
st.write(data.describe())

#duplicated
# duplicated_data = data[data.duplicated()]
# print(duplicated_data)

#drop duplicates
data = data.drop_duplicates()
st.header("Dataset after dropping duplicates")
st.write(data)

#Calculating mean 
columns = ['price','km_driven','overall_cost']
mean = data[columns].mean()
st.header("Mean Values")
st.write(mean)
# print(f'Mean : \n {mean}')
# #calculateing median
median = data[columns].median()
st.header("Median Values")
st.write(median)
# print(f'Median : \n {median}')
# #calculating mode
mode_columns = ['make_year','price','km_driven','overall_cost']
mode = data[mode_columns].mode()
st.header("Mode Values")
st.write(mode)
# print(f'Mode : \n {mode}')

#Handling missing values
#identifying columns with null or missing values
null_counts = data.isnull().sum()
st.header("Null values")
st.write(null_counts)
#filling null values of reg_year with not avaliable 
data['reg_year'].fillna('Not Avaliable',inplace=True)
data['engine_capacity(CC)'].fillna(data['engine_capacity(CC)'].mean(),inplace=True)
st.header("Dataset after filling missing values")
st.write(data.info())


#Error Correction
#ensuring correct datatypes
data['make_year'] = pd.to_numeric(data['make_year'],errors='coerce')
data['price'] = pd.to_numeric(data['price'],errors='coerce')
data['km_driven'] = pd.to_numeric(data['km_driven'],errors='coerce')
data['overall_cost'] = pd.to_numeric(data['overall_cost'],errors='coerce')
st.header("Dataset after correcting datatypes")
print(data.info())


#Normalization
scaler  = MinMaxScaler()
data[['price','km_driven','overall_cost']] = scaler.fit_transform(data[['price','km_driven','overall_cost']])
st.header("Dataset after normalization")
st.write(data)


#encoding categorical data
data['title_year'] = data['title'].str.extract(r'(\d{4})')
data['title_brand'] = data['title'].str.split().str[1]
data = data.drop(columns=['title'])
data = pd.get_dummies(data,columns=['title_brand'],drop_first=True)
st.header("Dataset after encoding categorical data")
st.write(data)


#Scaling
scaler = StandardScaler()
data[['price','km_driven','overall_cost','engine_capacity(CC)','make_year']] = scaler.fit_transform(data[['price','km_driven','overall_cost','engine_capacity(CC)','make_year']])
st.write(data)

#output data
output_file = r"C:\Users\Abhiyanshu\Downloads\pre-owned cars_cleaned.csv"
data.to_csv(output_file,index=False)
st.download_button(
    label="Download Cleaned Dataset",
    data=data.to_csv(index=False).encode('utf-8'),
    file_name='pre-owned_cars_cleaned.csv',
    mime='text/csv'
)
