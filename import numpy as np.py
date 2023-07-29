'''
import numpy as np

my_array = np.arange(6).reshape(2, 3)
print("Original array:")
print(my_array)


my_array[:, [2, 0]] = my_array[:, [0, 2]]
print("After swapping arrays the last column and first column:")
print(my_array) ''' 

'''
f = open("C:\\Users\sarth\OneDrive\Documents\#LAB\PY\import.txt","r")
print(f.read()) '''

'''
import numpy as np

a=np.array([(1,2,3,4,5,6)])

print(a.size)
print(a.shape)'''

'''
import numpy as np

a=np.array([(1,2,3,4,5,6)])

print(a.size)
print(a.shape)'''

'''
import numpy as np

a=np.array([(1,2,3,4,5,6)])
b=np.array([(1,2,3,4,5,6)])
c=a+b

print(c) '''


import numpy as np

a=np.array([(1,2,3),(4,5,6)])
print(a)

a=a.reshape(3,2)
print(a) 
