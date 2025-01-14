'''
Summary
Loading the Data: We loaded the Boston Housing dataset.

EDA: We explored the data and plotted the distribution of house prices.

Preprocessing: We scaled the features and checked for missing values.

Splitting the Data: We split the data into training and testing sets.

Training the Model: We trained a linear regression model.

Evaluating the Model: We evaluated the model using MAE, MSE, and R-squared.

Making Predictions: We made predictions on new data.
'''
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Loading the dataset
import pandas as pd
from sklearn.datasets import fetch_california_housing

# Loading the dataset
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
# MedHouseVal is the target variable (median house value)
df['MedHouseVal'] = california.target

print(df.head())

# -----------


# Plotting the distribution of the target variable
sns.histplot(df['MedHouseVal'], kde=True)
plt.title('Distribution of House Prices')
plt.xlabel('Median Value (in $100,000s)')
plt.ylabel('Frequency')
plt.show()


# -----------


# Checking for missing values
print(df.isnull().sum())

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop('MedHouseVal', axis=1))

# Defining the features (X) and target variable (y)
X = pd.DataFrame(X_scaled, columns=california.feature_names)
y = df['MedHouseVal']


# Splitting the data -----------------------

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# -----------------------------------------

# Creating and training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

print(f'Coefficients: {coefficients}')
print(f'Intercept: {intercept}')

# ---------------------------

# Making predictions on the test data
y_pred = model.predict(X_test)

# Calculating evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'R-squared: {r2}')

# ---------------------------
# Creating a DataFrame for new data points
new_data = pd.DataFrame({
    'MedInc': [8.3252], 'HouseAge': [41.0], 'AveRooms': [6.9841], 'AveBedrms': [1.0238],
    'Population': [322.0], 'AveOccup': [2.5556], 'Latitude': [37.88], 'Longitude': [-122.23]
})

# Scaling the new data
new_data_scaled = scaler.transform(new_data)

# Making predictions
predicted_price = model.predict(new_data_scaled)
print(f'Predicted House Price: ${predicted_price[0] * 100000:.2f}')


# # Plotting the regression line
# plt.scatter(df['MedHouseVal'], df['MedInc'])
# plt.plot(df['MedHouseVal'], model.predict(X), color='red')
# plt.xlabel('Median House Value')
# plt.ylabel('Median Income')
# plt.show()
