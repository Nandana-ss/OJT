# Fit a linear regression model using scikit-learn for the data points x = [1, 2, 3, 4, 5] and y = [2, 3, 5, 7, 11]. Predict the value of y when x = 6.
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 3, 5, 7, 11])

model = LinearRegression()
model.fit(x, y)

x_new = np.array([[6]])
y_pred = model.predict(x_new)
print(f'The predicted value of y when x = 6 is {y_pred[0]}')
