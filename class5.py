# difference between variable length argument and variable length keyword argument also check symbols
# what is keyword argument . when do we use this and where is it used
def student(name, age, course ):
    print("Name:",name)
    print("Age :" ,age)
    print("Course:",course)
student(course='MCA', name="Divya",age=22)#keyword argument
print()
student("shreya",21,"MTech")# positional argument


#student details using variable length keyword arg **kwargs
def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

student_details(name='Rahul',age=22,course='MCA',semester=3)

#combining both *args and **kwargs
def students(*subjects, **details):  #sub-variable len arg , detail - var len kwardg
    print("subjects:")
    for subject in subjects:
        print("-", subject)
    print("/n student details")
    for key, value in details.items():
        print(key, ":", value)
students("python","dbms","machine learning",name="rahul",semester=2)

#return values - 
#returning multiple values

def add_print(a,b):
    print(a+b)
def add_return(a,b):
    return a+b
result1=add_print(30, 100) #displays the result but return none
print("result of print:",result1)

result2=add_return(10,20)
print("result of return:",result2)

#returning multiple values   
def result(marks):
    total = sum(marks)
    percentage=total/len(marks)
    return total, percentage 

marks=[85,45,67,86,78]
total, percentage = result(marks)
print("total:",total)
print("percentage:",percentage)
# try:dynamical cal or decide with * marks, parameter , if its not variable then wt could u do to dynamically call
def result(marks):
    total = sum(marks)
    percentage=total/len(marks)
    return total, percentage 

total, percentage = result([85,90,56,78])
print("total:",total)
print("percentage:",percentage)

#scope of variable- 1.Global variable 
#2.Local variable
#what is difference when global keyword is used for a variable

#check balance using global
balance=10000
def deposit(amt):
    global balance
    balance +=amt
deposit(2000)
print("balance=",balance)
