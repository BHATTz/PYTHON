import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb

data = pd.read_csv("C:\\Users\sarth\OneDrive\Documents\#LAB\PY\heart.csv")

print(data.corr())

dataplot = sb.heatmap(data.corr(), cmap="YlGnBu", annot=True)

mp.show()