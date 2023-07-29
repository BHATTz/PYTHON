class a(object):
    def init(self):
        print("enter Student details")
        self.Name=""
        self.roll=""
        self.marks=""
        
    def b(self):
            self.Name=input("Enter Name:") 
            self.roll=int(input("Enter roll:"))
            self.marks=input("Enter marks:")
            
    def display(self):
        print("Name :",self.Name)
        print("roll :",self.roll)
        print("marks:",self.marks)
 
L=[]
num= int(input("Enter the no. of students: ")) 
for i in range(num): 
    a=a() 
    a.b() 
    L.append(a) 

for i in range(num): 
    print("--------------------")
    L[i].display()
    print("--------------------")