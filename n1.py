'''
import numpy as np
arr= np.array([4,5,8,9,11])
print(arr)'''

import numpy as np
my_array= np.arange(12).reshape(4,3)
print("orignal array:")
print(my_array)
my_array[:,[2,0]] = my_array[:,[0,2]]
print("after swapping arrays the last column and first")
print(my_array)