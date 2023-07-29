import pandas as pd
df = pd.read_csv("C:\\Users\sarth\OneDrive\Documents\#LAB\PY\heart.csv") 
mean1 = df['trestbps'].mean()
sum1 = df['trestbps'].sum()
max1 = df['trestbps'].max()
min1 = df['trestbps'].min()
count1 = df['trestbps'].count()
median1 = df['trestbps'].median() 
std1 = df['trestbps'].std() 
var1 = df['trestbps'].var() 
mode1 = df['trestbps'].mode() 
print('mean trestbps: ' + str(mean1))
print('sum of trestbps: ' + str(sum1))
print('max trestbps: ' + str(max1))
print('min trestbps: ' + str(min1))
print('count of trestbps: ' + str(count1))
print('median trestbps: ' + str(median1))
print('std of trestbps: ' + str(std1))
print('var of trestbps: ' + str(var1))
print('mode trestbps: ' + str(mode1))


# import statistics
# data1 = [1, 3, 4, 5, 7, 9, 2]
# x = statistics.mean(data1)
# print("Mean is :", x)