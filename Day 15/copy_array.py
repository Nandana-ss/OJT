import numpy as np

arr=np.array([5,8,9,1,5])
copy_array=np.copy(arr)
copy_array[2]=7
print("Original array: ",arr)
print("Copied array: ",copy_array)