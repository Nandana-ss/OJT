import numpy as np

arr=np.array([9,4,6,7,2])
view_arr=arr.view()
view_arr[3]=5
print("Original array after modification: ",arr)
print("modified array:",view_arr)
