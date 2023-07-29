'''
def find_gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           gcd = i
    return gcd

first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

print('GCD of %d and %d is %d' %(first, second, find_gcd(first, second)))

lcm = first * second / find_gcd(first, second)
print('LCM of %d and %d is %d' %(first, second, lcm)) '''


n=input(" Enter a number ")
sum=0
for i in range(0,len(n)):
  sum=sum+pow(int(n[i]),3)

print("Sum of cube of digits  : ",sum)
if(sum==int(n)):
  print("Digits are matching to cube  : ", n)
else:
  print("Digits are NOT matching to cube : ", n)

my_list=[]
for n in range(100,1000): # increase this range
  sum=0
  my_str=str(n)
  k=len(my_str)
  for i in range(0,k):
    sum=sum+pow(int(my_str[i]),3)
  
  if(sum==int(n)):
    my_list.append(n)
print("Highest number : ",max(my_list))
print("Lowest  number : ",min(my_list))