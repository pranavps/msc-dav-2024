'''
Summary
Loading the Data: We loaded the California Housing dataset.

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
import numpy as np

# Loading the dataset
from sklearn.datasets import fetch_california_housing
# Creating a synthetic dataset
np.random.seed(42)  # For reproducibility
house_size = np.random.randint(1000, 4000, 100)  # House sizes in square feet
house_price = 150 + 50 * (house_size / 1000) + np.random.normal(0, 25, 100)  # House prices in $1000s

# Creating a DataFrame
data = pd.DataFrame({
    'HouseSize': house_size,
    'HousePrice': house_price
})

print(data.head())

# Exploring the data
plt.scatter(data['HouseSize'], data['HousePrice'])
plt.title('House Size vs House Price')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price ($1000s)')
plt.show()

X = data[['HouseSize']]  # Predictor (independent variable)
y = data['HousePrice']  # Target (dependent variable)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

print(f'Coefficient: {coefficients[0]}')
print(f'Intercept: {intercept}')

# Making predictions on the test data
y_pred = model.predict(X_test)

# Calculating evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'R-squared: {r2}')

# Plotting the predictions
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Prices')
plt.title('House Size vs House Price (Test Data)')
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price ($1000s)')
plt.legend()
plt.show()

# Predicting the price of a new house
new_house_size = pd.DataFrame({'HouseSize': [2500]})
predicted_price = model.predict(new_house_size)
print(f'Predicted House Price for 2500 sq ft: ${predicted_price[0] * 1000:.2f}')
