# Convert the array into a 1D array
import numpy as np
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array_1d = array_3d.flatten()
print(array_1d)
