'''from re import X
from tkinter import Y
from typing_extensions import Self'''


'''class add_sub:
    def__init__(Self,x,y):
    Self.x=X
    Self.y=Y
    def add(self):
        return self.x + self.y
    def subtract Self.x - Self.y'''

'''  #A simple python function
def fun():
        print("welcome to MCA 1st Semester")
# to call a function
fun()'''

#refining and calling function with parameters

'''def add(num1: int, num2: int) -> int:
    num3 = num1 + num2
    return num3
num1, num2 = 7, 10
ans=add(num1,num2)
print(f"The addition of {num1} and {num2} results {ans} ,")'''

'''#A simple python function to check
#whether x is even or odd
def evenodd(x):
    if(x % 2==0):
        print("even")
    else:
        print("odd")

evenodd(2)
evenodd(3)'''

'''#python program to demonstrate
#default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

#we call myFun() with only
#arguments
myFun(10)'''

'''#python program to demonstrate keyword arguments
def student(firstname, lastname):
    print(firstname, lastname)

#keyword arguments
student(firstname='MCA', lastname='1st Semester')
student(lastname='3rd semester', firstname='M.Tech')'''

#Python program to illustrate 
#*args for variable number of arguments

'''def myFun(*args):
    for arg in args:
        print(arg)
myFun('UIC', 'Welcome', 'to', 'MCA 1st Semester')'''

'''#Python program to illustrate 
# *kwargs for variable number of keyword arguments

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s ==%s" % (key, value))

#driver code
myFun(first='Python', mid='Class', last='Best')'''

'''#Recursion function
def factorial(x):
    """This is a recursive function to find the factorial of an integer"""
    if x==1:
        return 1
    else:
        return (x * factorial(x-1))
num = 7
print("The factorial of",  num, "is", factorial(num))'''

#Python lambda function example
#lambda returns a function object
str1='Python class'
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))

