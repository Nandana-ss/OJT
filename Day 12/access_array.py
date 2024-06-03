import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
element = arr[1,2]
print(element)

row = arr[1,:]
print("second row: ",row)

column = arr[:,1]
print("second column: ",column)

# slicing
slice_array= arr[0:2,1:3]
print(slice_array)