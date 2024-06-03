import numpy as np
# 1 - D array
arr_1 = np.array([1,2,3,4,5,6])
print("1-d array: ",arr_1)

# 2 - D
arr_2 = np.array([[1,2,3],[4,5,6]])
print("2-d array: ",arr_2)

arr_3 = np.array([[[1,2,3],[4,5,6]]])
print("3-d array: ",arr_3)

# array with ones
arra_ones = np.ones((2,4))
print(arra_ones)

arra_zero = np.zeros((3,4))
print(arra_zero)

# array with range
arr_range = np.arange(10)
print("range array: ",arr_range)