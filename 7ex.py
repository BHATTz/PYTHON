# n1 = int(input("enter first number :"))
# n2 = int(input("enter second number :"))
# x = n1
# y = n2

# while(n2!=0):
#   t = n2
#   n2 = n1 % n2
#   n1 = t

# gcd=n1
# print("gcd of {0} and {1} = {2}".format(x,y,gcd))
# lcm = (x*y)/gcd
# print("lcm of {0} and {1} = {2}".format(x,y,lcm))
# sm = x+y
# print("sum of {0} and {1} = {2}".format(x,y,sm))

#
n=input(" Enter a number ")
sum=0
for i in range(0,len(n)):
  sum=sum+pow(int(n[i]),3)

print("Sum of cube of digits  : ",sum)
if(sum==int(n)):
  print("Digits are matching to cube  : ", n)
else:
  print("Digits are NOT matching to cube : ", n)

#
my_list=[]
for n in range(100,1000):
  sum=0
  my_str=str(n)
  k=len(my_str)
  for i in range(0,k):
    sum=sum+pow(int(my_str[i]),3)
  
  if(sum==int(n)):
    my_list.append(n)
print("Highest number : ",max(my_list))
print("Lowest  number : ",min(my_list))