'''
import numpy as np
a = np.array([1,2,3])
print(a) '''

'''
import numpy as np
a = np.array([1,2,3]),([4,5,6])
print(a)'''

'''
import numpy as np
import time 
import sys
S=range(500)
print(sys.getsizeof(5)*len(S))
D=np.arange(500)
print(D.size*D.itemsize)'''

'''
import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)'''

'''
import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.dtype)'''

'''
import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.max())
print(a.sum()) '''

'''
import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.sum())'''


import numpy as np
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n",arr)
arr = np.array([[1, 2, 3],[4, 5, 6]])
print("Array with Rank 2: \n", arr)
arr = np.array((1, 3, 2))
print("\nArray created using""passed tuple:\n", arr)

