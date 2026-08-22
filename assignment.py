#Pattern Problems

"""1.	Increasing Right Triangle
*
**
***
****
***** """
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print() 

""" 2.	Decreasing Right Triangle
*****
****
***
**
* """
n=int(input("enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

""" 3.	Right-Aligned Increasing Triangle
*
* *
* * *
* * * *
* * * * * """
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print() 

""" 4.	Right-Aligned Decreasing Triangle
* * * * *
* * * *
* * *
* *
* """
n=int(input("enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print() 

"""Pyramid Paflerns
5.	Full Pyramid
     *
    ***
   *****
  *******
 ********* """
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print() 

# 6. inverted pyramid
n=int(input("enter the number:"))
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print() 

# dimond logic
n=int(input("enter the number:"))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()

#8. hallow pyramid
n=int(input("enter the number:"))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    
    if i==1:
        print("*",end=" ")
    elif i==n:
        for k in range(1,2*i):
            print("*",end=" ")
    else:
        print("*",end=" ")
        for k in range(1,2*i-2):
            print(" ",end=" ")
        print("*",end=" ")
    
    print() 

#9. complete  square
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()

#10. Hollow Square

n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 11. number square
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

#12. Same Number Square
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

#13. Number Paflerns
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#14. decreasing number triangle
n=int(input("enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 

#15. repeated number triangle
n=int(input("enter the number:"))
for i in range(1,n):
    for j in range(1,i+1):
        print(i,end=" ")
    print() 

#16.reverse number triangle
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(5,5-i,-1):
        print(j,end=" ")
    print()

#17. continious number triangle
n=int(input("enter the number:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print() 

#18. number pyramid pattermn 
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()

##Alphabet Paflerns

#19. alphabet increasing triangle
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print() 

#20. Repeated Alphabet Triangle 
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print() 

#21. continious alphabet triangle
n=int(input("enter the number:"))
num=65

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(num),end=" ")
        num+=1
    print() 

#22. reverse alphabet triangle 
n=int(input("enter the number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print() 

##Special Paflerns

#23.x pattern
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==n-i+1:
            print("*",end="")
        else:
            print(" ",end="")
    print() 

#24. + pattern
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==(n+1)//2 or j==(n+1)//2:
            print("*",end="")
        else:
            print(" ",end="")
    print() 

#25. hollow dimond

n=int(input("enter the number:"))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    print("*",end="")
    if i>1:
        for k in range(1,2*i-2):
            print(" ",end="")
        print("*")
    else:
        print()

for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(" ",end="")
    print("*",end="")
    if i>1:
        for k in range(1,2*i-2):
            print(" ",end="")
        print("*")
    else:
        print() 
#26. Hourglass Pattern
n=int(input("enter the number:"))

for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

for i in range(2,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

#27. Filtering based on Condition
# Filter numbers greater than 21
#Input: numbers = [12, 45, 7, 23, 56, 18, 90]
#Output: large_numbers = [45, 23, 56, 90]

numbers=[12,45,7,23,56,18,90]
result=[]

for i in numbers:
    if i>21:
        result.append(i)

print("Output:",result) 

""" 28. 28.	Reversing a String with For Loop original_str = "Python"
reversed_str = "nohtyP" """


original_str="Python"
reversed_str=""

for i in range(len(original_str)-1,-1,-1):
    reversed_str+=original_str[i]

print("original_str =",original_str)
print("reversed_str =",reversed_str)



import math

# Delivery partners
partners = [
    {
        "id": "D101",
        "name": "Rahul",
        "location": (12, 11),
        "status": "Available",
        "deliveries": 8,
        "rating": 5,
        "idle_time": 10
    },
    {
        "id": "D102",
        "name": "Anu",
        "location": (9, 8),
        "status": "Available",
        "deliveries": 4,
        "rating": 4,
        "idle_time": 15
    },
    {
        "id": "D103",
        "name": "Kiran",
        "location": (9, 8),
        "status": "Busy",
        "deliveries": 4,
        "rating": 3,
        "idle_time": 20
    },
    {
        "id": "D104",
        "name": "John",
        "location": (11, 9),
        "status": "Available",
        "deliveries": 2,
        "rating": 5,
        "idle_time": 25
    }
]

# Restaurant location
restaurant = (6, 7)


# Function to calculate distance
def distance(partner):
    x1, y1 = restaurant
    x2, y2 = partner["location"]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Step 1: Select only available partners
available = [
    p for p in partners
    if p["status"] == "Available"
]

# Step 2: Find minimum deliveries
min_deliveries = min(
    p["deliveries"] for p in available
)

candidates = [
    p for p in available
    if p["deliveries"] == min_deliveries
]

# Step 3: Highest rating
max_rating = max(
    p["rating"] for p in candidates
)

candidates = [
    p for p in candidates
    if p["rating"] == max_rating
]

# Step 4: Nearest partner
min_distance = min(
    distance(p) for p in candidates
)

candidates = [
    p for p in candidates
    if distance(p) == min_distance
]

# Step 5: Longest idle time
selected = max(
    candidates,
    key=lambda p: p["idle_time"]
)

# Assign delivery
selected["status"] = "Busy"
selected["deliveries"] += 1

print("Delivery Assigned to", selected["id"])
print("Partner Name:", selected["name"])
print("Status:", selected["status"])
print("Deliveries Today:", selected["deliveries"])