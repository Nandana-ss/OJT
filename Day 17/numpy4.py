# A scatter plot with 1000 dots
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)  # For reproducibility
x = np.random.rand(1000)
y = np.random.rand(1000)
plt.scatter(x, y, color='blue', marker='o', alpha=0.5)
plt.title('Scatter Plot with 1000 Dots')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
