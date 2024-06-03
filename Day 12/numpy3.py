import numpy as np
orig_array = np.array([1,2,3,4,5,6])
print("original array: ",orig_array)

view_array = orig_array.view()
print("view array: ",view_array)
view_array[2] = 30
print("Modified view array: ",view_array)
print("original array after modification of view: ",orig_array)

# copy
copy_arr = orig_array.copy()
print("Copy of the array: ",copy_arr)
copy_arr[2] = 3
print("Copy of the array after modification: ",copy_arr)
print("Original array after copy modificaton: ",orig_array)