import numpy as np
import matplotlib.pyplot as plt
N = 10
x = np.random.rand(N)
y = np.random.rand(N)
colors = ('red')
plt.scatter(x, y, c=colors)
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()