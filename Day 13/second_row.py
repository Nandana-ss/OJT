#  Access the element on the 2nd row, 5th column in the array
import numpy as np
arr = np.array([[1, 2, 3, 4, 5],
                [6,7,8,9,10],
                [11,12,13,14,15]])
element = arr[1:2,4]
print(element)