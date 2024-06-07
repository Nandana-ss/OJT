# Check if the returned array is a copy or a view
import numpy as np
arr = np.array([1,2,3,4,5])
print("Original array: ",arr.base)
view_arr = arr[0:2]
print("View arr .base:",view_arr.base)