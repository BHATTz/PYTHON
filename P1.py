class first():  
    def a(self):  
        print("This is a Lab class")  
  
    def b(self):  
        print("PYTHON")  
  
    def c(self):  
        print("Professor")  
  
class second():  
    def a(self):  
        print("This is a Theory class")  
  
    def b(self):  
        print("Kotlin")  
  
    def c(self):  
        print("Assistent Professor")  
  
obj1 = first()  
obj2= second()  
for read in (obj1, obj2):  
    read.a()  
    read.b()  
    read.c()