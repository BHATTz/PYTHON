def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        return True

def ptwins(start, end):
    for i in range(start, end):
        j=i+2
        if(prime(i) and prime(j)):
            print(i,"and",j) 
ptwins(2,1000)