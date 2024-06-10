# Use the scatter() method to draw a scatter plot diagram
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 3, 4, 5, 6, 7, 8, 9])
plt.scatter(x, y, color='blue', marker='o')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
