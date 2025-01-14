# Linear regression demo 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample DataFrame
data = {'Age': [28, 22, 35, 40, 50, 30, 31, 25, 34, 28],
        'Price': [1000, 800, 1200, 1500, 2000, 1100, 900, 700, 1300, 1000]}
df = pd.DataFrame(data)

# Scatter plot
plt.scatter(df['Age'], df['Price'])
plt.xlabel('Age')
plt.ylabel('Price')
plt.show()

# Linear regression
coefficients = np.polyfit(df['Age'], df['Price'], 1)
intercept = coefficients[1]
slope = coefficients[0]
print(f'Linear Regression: y = {slope}x + {intercept}')

# Plotting regression line
x = np.linspace(df['Age'].min(), df['Age'].max(), 100)
y = slope * x + intercept
plt.plot(x, y, color='red')
plt.show()

# Residuals
residuals = df['Price'] - (slope * df['Age'] + intercept)
print(f'Residuals: {residuals}')

# R-squared
r_squared = np.corrcoef(df['Price'], df['Age'])[0, 1] ** 2
print(f'R-squared: {r_squared}')

# Adjusted R-squared
adjusted_r_squared = 1 - (1 - r_squared) * (len(df) - 1) / (len(df) - 2)
print(f'Adjusted R-squared: {adjusted_r_squared}')

# Mean squared error
mean_squared_error = np.mean(residuals ** 2)
print(f'Mean squared error: {mean_squared_error}')

# Root mean squared error
root_mean_squared_error = np.sqrt(mean_squared_error)
print(f'Root mean squared error: {root_mean_squared_error}')

# Mean absolute error
mean_absolute_error = np.mean(np.abs(residuals))
print(f'Mean absolute error: {mean_absolute_error}')

# Median absolute error
median_absolute_error = np.median(np.abs(residuals))
print(f'Median absolute error: {median_absolute_error}')

# ---------------------------

print("---------------------------")

# Sample DataFrame
data = {
    'Hours_Studied': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Sleep_Hours': [7, 6, 5, 5, 4, 4, 3, 3, 2, 3],
    'Test_Score': [75, 78, 85, 90, 95, 96, 97, 98, 99, 100, 100]
}
df = pd.DataFrame(data)

# Defining the predictors and response variable
X = df[['Hours_Studied', 'Sleep_Hours']]
y = df['Test_Score']

# Creating and training the model
model = LinearRegression()
model.fit(X, y)

# Coefficients
coefficients = model.coef_
intercept = model.intercept_

# Creating a DataFrame for the new data point with valid feature names
new_data = pd.DataFrame({'Hours_Studied': [4], 'Sleep_Hours': [5]})
predicted_score = model.predict(new_data)

print(f'Coefficients: {coefficients}')
print(f'Intercept: {intercept}')
print(f'Predicted Test Score: {predicted_score[0]}')

print("---------------------------")
