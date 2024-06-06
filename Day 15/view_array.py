import numpy as np

arr=np.array([8,6,4,3,1])
view_arr=arr.view()
arr[2]=0
print("original array:",arr)
print("modified array:",view_arr)