#bubble sort
#a=list(map(int,input("enter the numbers:").split()))
#for i in range(len(a)):
#    for j in range(i,len(a)-1):
#        if a[j]>a[j+1]:
#            a[j],a[j+1]=a[j+1],a[j]
#print("sorted list is:",a)

## continue statement
#for i in range(10):
#    if i==5:
#        continue
#    print(i)

## pass statement
#for i in range(10):
#    if i==5:
#        pass
#    print(i)

##print prime numbers between given range
#a=int(input("enter the number to be checked:"))
#for i in range(2,a):
#    if a%i==0:
#        print(f"{a} is not prime")
#        break
#else:
#    print(f"{a} is prime")
import math
#m=int(input("enter the starting range:"))
#n=int(input("enter the ending range:"))
#for i in range(m,n):
#    if i<2:
#        continue
#    y=int(math.sqrt(i))+1
#    for j in range(2,y): # use root n to optimise still like n^1/2
#        if i%j==0:
"""           break
    else:
        print(i,end=" ")"""


## take input until 0 is entered and print the sum of all numbers entered
"""total=0
num=int(input("enter the number:"))
while num!=0:
    total+=num
    num=int(input("enter the number(0 to stop):"))
print(f"total is:{total}")"""

##factorial of a number
"""num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact*=i 
print("factorial of ",num,"is:",fact)"""

##print pattern
"""for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""

##print piramid pattern
for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="*")
    for k in range(1,i+1):
        print("*",end=" ")
    print()