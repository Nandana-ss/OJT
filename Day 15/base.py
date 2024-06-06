import numpy as np


original_array = np.array([1, 2, 3, 4, 5])
print("original_array.base:", original_array.base)
view_array = original_array[0:2]
print("view_array.base:", view_array.base)
