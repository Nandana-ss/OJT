#  Convert 1D array with 8 elements to 3D array with 2x2 elements
import numpy as np
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8])
array_3d = array_1d.reshape((2, 2, 2))
print(array_3d)
