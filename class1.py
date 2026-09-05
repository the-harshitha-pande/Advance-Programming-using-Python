#when to use shorthand if
#shorthand if statements and ternary operators should be used when:
#the condition 

##short hand if 
"""age = int(input("enter your age:"))
if age >=18:
    print("you are eligible to vote")"""

##short hand if else
"""marks=int(input("enter your marks:"))
print(f"pass with score: {marks}") if marks>=35 else print(f"fail with score: {marks}")"""

##assigning value based on if else
"""result="pass" if marks>=35 else "fail"
print(f"result is: {result}")"""

#MULTIPLE condition combining in one line
"""amount=int(input("enter your amount:"))
discount=0.1 if amount>10000 else 0.05 if amount>5000 else 0.02
print(f"discount is: {discount*100}%")"""

#combining multiple condition 
"""age=int(input("enter your age:"))
is_stud=False
dscnt_code=True
if age>=18 or age> 65 and not is_stud or dscnt_code:
    print("discount applies")"""

#leap year
"""year=int(input("enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print(f"{year} is a leap year") 
else:
    print(f"{year} is not a leap year")"""

#leapyear using shorthand if else
"""year=int(input("enter the year:"))
leapyear=print("leap")if year%4==0 and year%100!=0 or year%400==0 else print("not leap")"""

#using paranthesis in shorthand
"""temperature=25
is_rainnig=False
is_weekend=True

if (temperature>20 and not is_rainnig) or is_weekend:
    print("great day for outdoor activities")"""

##multiple conditions
"""marks=int(input("enter your marks:"))
print("O") if marks>=90 else\
print("A") if marks>=80 else\
print("B") if marks>=70 else\
print("C") if marks>=60 else\
print("D") if marks>=50 else\
print("F")"""

##finding or generating fibonaccii series using while loop
"""a,b=0,1
i=0
leng=int(input("enter the length of fibonaccii series:"))
while i<leng:
    print(a,end="") 
    a,b=b,a+b
    i+=1"""

#reverse using while loop
"""count=5
while count>0:
    print(count)
    count-=1"""
"""for i in reversed(range(5)):
    print(i) """ 

# sorting the list in ascending order
"""nums=[5,2,9,1,7]
for num in sorted(nums):
    print(num)  """

##difference bt sort n sorted

# git add .
# git commit -m "Updated project"
# git push