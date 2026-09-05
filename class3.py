#in a for loop how many arguments will be there - 3 start, steps,end

""" n = int(input("Enter the number: "))
value = 1

for i in range(1, 11, 1):
    print(n * value)
    value = value + 1"""

#reversed
"""n = int(input("Enter the number: "))
value = 1

for i in range(10, 0, -1):
    print(n * i)"""


# assignment 2 -> patterns should be done here and write tht in notes . make 2 parts - code and output
#delivery system assignment 

#Function
""" reusable block of code which can be called multiple times in a program.
 It is used to perform a specific task.
 helps avoide code repetition and redundancy. It is case sensitive
 It helps to reduce the code redundancy and makes the code more organized and readable. """

#function name
"""a function name must start with a letter or underscore and can contain letters,
 numbers, and underscores. It should not be a reserved keyword in Python. 
 Function names r case sensitive."""

#





#different categories of arguments. is there difference between parameters and arguments? 
# yes, parameters are variables defined in the function definition,
#  while arguments are the values passed to the function when it is called.
# actual arguments are in function call and formal arguments are in function definition.

#different types of cases   
"""
1.Snake Case: all letters are lowercase and words are separated by underscores 
 (e.g., my_variable)(to remember - snake dosnt hv bones)
2. Camel Case: the first letter of each word is capitalized except for the first word
  (e.g., myVariable)(to remember - camel has humps)
3. Pascal Case: the first letter of each word is capitalized
  (e.g., MyVariable)(to remember - each word starts with a capital letter)"""

#different types of arguments
"""
positional arguments: the values are assigned to the parameters based on their position
 in the function call.
keyword arguments: the values are assigned to the parameters based on their names
 in the function call.
Multiple arguments: the function can accept multiple arguments of different types.
(arbitrary number of arguments)
"""
"""
def greet():
    print("Hello, welcome to python programming!")
greet()  # calling the function

#calculate area of circle
def calculate_area():
    radius = float(input("Enter the radius e: "))
    area = 3.14 * radius *radius
    print("area:", area)"""
"""
def greeting():
    return "Hello, Iam Harshitha"
print(greeting())"""

#example for default arguments- calculate sum)
"""def add(a,b): #a,b are arguments
    print("sum:",a+b)
add(10,20) #10,20 are parameters """

"""default arguments can find mismatch in number of arguments and parameters.
  if we give less number of arguments than parameters,
  then default values will be used for the missing arguments."""

#students details- how would you u solve mismatch of number of argumenets in defination to number od parameters
"""def student(name,message="welcome to amrita",course="Mca"):
    print(message """