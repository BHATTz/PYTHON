import matplotlib.pyplot as plt
import numpy as np

#create graph
x = np.array([1,2,3,4])
y = x*2
plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("graph")
plt.show()

#change the graph line add 2 lines in x axis.
plt.plot(x,y)
x1 = [2,4,6,8]
y1 = [3,5,7,9]
plt.plot(x1, y1, '-.')
plt.show()

#fill the color
plt.fill_between(x,y,y1,color='green',alpha=0.5)
plt.show()