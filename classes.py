'''class student:
    def data(d):
        d.roll_no=str(input("Enter the roll no. of student:- "))
        d.Name=str(input("Enter the name of student:- "))
        d.Class=str(input("Enter the class:-"))
    def show(d):
        print("\n")
        print("your data is shown below")
        print("\nThe roll no. is: ",d.roll_no)
        print("the Name is: ",d.Name)
        print("The Class is: ",d.Class)
s1=student()
s1.data()
s1.show()

class add_sub:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    def subtract(self):
        return self.x-self.y
if __name__=='__main__':
    x=11
    y=7
    opp=add_sub(x,y)
    print(f"{x}+{y}={opp.add()}")
    print(f"{x}-{y}={opp.subtract()}")


class students:
    def __init__(self):
        self.a=int(input("enter the number: "))
        self.b=int(input("enter the  number: "))
    def show(self):
        c=self.a+self.b
        d=self.a-self.b
        print(c)
        print(d)
s1=students()
s1.show()

class student:
    def fac(a):
        a.f=int(input("enter the number"))
        fact=1
        for i in range (1,a.f+1):
           fact=fact*i
        print(fact)
s1=student()
s1.fac()'''

'''
class student:
    def __init__(a):
        a.f=int(input("enter the number"))
        a.fact=1
        for i in range (1,a.f+1):
           a.fact=a.fact*i
    def show(a):
        print(a.fact)
s1=student()
s1.show()

import keyword
print(keyword.kwlist)

x=None
print(type(x))

class student:
    def fun(li):
        li.li=[1,2,3,4]
        for num in li.li:
          print(num**2)
s1=student()
s1.fun()   '''

'''
from re import A


class add_sub:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a 
        self.b = b 
    def add(self) :
        return self.x + self.y
    def subtract(self) :
        return self.x - self.y
    def multiply(self) :
        return self.a * self.b
    def divide(self) :
        return self.a / self.b      
    
if __name__ == '__main__':
    x = 11
    y = 7
    a = 10
    b = 2

    opp = add_sub(x,y,a,b)

    print(f'{x} + {y} = {opp.add()}')
    print(f'{x} - {y} = {opp.subtract()}')
    print(f'{a} * {b} = {opp.multiply()}')
    print(f'{a} / {b} = {opp.divide()} '''

'''
num = 2
for i in range(1, 11):
   print(num, 'x', i, '=', num*i) '''


class cylinder:
    pi = 3.14
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

if __name__=='__main__':
    c1 = cylinder(4, 20)
    c2 = cylinder(10, 50)
    
    print(f'Pi for c1:{c1.pi} and c2:{c2.pi}')
    print(f'radius for c1:{c1.radius} and c2:{c2.radius}')
    print(f'height for c1:{c1.height} and c2:{c2.height}')
    print(f'pi for both c1 and c2 is: {cylinder.pi}') 