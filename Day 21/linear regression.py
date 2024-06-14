import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

height = np.array([150, 160, 164, 165, 173]).reshape(-1,1)
weight = np.array([50, 65, 63, 68, 72])
model = LinearRegression()
model.fit(height, weight)
w_pred = model.predict(height)
print("intercepts are",model.intercept_)
print(f"Coefficients : {model.coef_[0]} ")

plt.scatter(height, weight, color = 'blue')
plt.plot(height, w_pred, color = 'red')
plt.xlabel("height")
plt.ylabel("weight")
plt.title('Linear regression')
plt.show()
