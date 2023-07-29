'''
import numpy as np
import matplotlib.pyplot as plt

data = {'Web UI':20, 'ADBMS':15, 'CN':30,
		'Python':35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(courses, values, color ='green',
		width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()  '''

'''
import matplotlib.pyplot as plt

labels = 'Python', 'CN', 'ADBMS', 'Web UI'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()  '''

import matplotlib.pyplot as plt
import numpy as np

def plot_parabola():

 x = np.linspace (-10, 10, 1000)
 y = x**2
 fig, ax = plt.subplots()
 ax.plot(x, y)

plot_parabola()
plt.show()