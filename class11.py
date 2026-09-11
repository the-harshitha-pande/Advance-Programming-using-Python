## DEBUGGING TECHNIQUES
"""
debugging is process of identifying, analysing and correcting errors(bugs) in a process

debugging is an essential programming skill because real-world software may fail due to:
incorrect program logic
invalid user input
runtime exceptions
incorrect variable values
function-call errors
file not resource issues- importing respective module or library 

unseen or unknowly missed error , finding them and handling them is what debugging in simple words

different types of debugging techniques are:
1. exception handling: using try and except block to handle errors and exceptions in the code.
2. assertion: using assert statement to check for conditions that should be true in the code, checking correctness.
3. logging: logging has certain parameters to check the correctnss of programusing logging module to log messages and errors in the code, helps to track the flow of the program and identify issues.
4. breakpoint: using breakpoint() function to pause the execution of the code at a specific point temporarly, allows to inspect the variables and state of the program. and continued through pdb module to step through the code and identify issues.
5. call-stack method:
6. raise: expecting that we might face an error , this can be called through try-catch exception. 
does python has default debugger?
PDB- python debugger - check and visit state to understand its state also

1. Assertion :
assertion is a debugging technique that involves checking for conditions that should be true in the code. 
It is used to catch errors early in the development process and ensure that the program is functioning as expected.
 
syntax of assert statement:
assert condition, message
"""

#1. assertion code
def calculate_average(numbers):
    assert len(numbers) > 0, "List of numbers cannot be empty"
    return sum(numbers) / len(numbers)

number=[10, 20, 30, 40, -1]
print(calculate_average(number)) # got output of average

# # empty list
def calculate_average(numbers):
    assert len(numbers) > 0, "List of numbers cannot be empty"
    return sum(numbers) / len(numbers)

number=[]
print(calculate_average(number)) # error occurs and assertion error is raised with message "List of numbers cannot be empty"

# 2. LOGGING:
"""
the logging module records about program execution 
unlike print(), logging can record message based on sevirity level.

common      logging levels:
debug      detailed info for debugging
info        general information about program execution
warning     indicate possible problem
error       indicate an error occured
critical   serious failure indicated
"""
#code for logging
import logging

#this configures how the message is displayed
logging.basicConfig(
    level=logging.DEBUG,                          #sets the minimum logging level to DEBUG, so all messages of this level and above will be displayed   
    format=' %(levelname)s - %(message)s'         #this determines how the log messages are formatted, including the logging level and the message itself
)

logging.debug("program started")
age= int(input("Enter your age: "))
logging.info(f"Age entered: {age}")               #record the value entered by user
if age<18:
    logging.warning("Age is below elegibility criteria")
logging.debug("program ended")

## 3. Python Debugger (PDB):
"""
python provides a built in debugger called pdb

it allows the programmer to :
-pause program execution 
- execute the program step by step
- inspect the values of variables at different points in the program


command             meaning
'n'                execute the next line of code
's'                step into a function call
'c'                continue execution until the next breakpoint
'p variable'       print the value of a variable
'l'                list the current line of code and surrounding lines
'bt'               print the call stack to see the sequence of function calls that led to the current point in the program
'q'                quit the debugger and enters to terminal again
'w'                show the current line and the lines around it entire call stack
"""

#code for pdb
import pdb
marks = [85, 90, 78]
total= sum(marks)
pdb.set_trace()  
average=total/len(marks)
print("Average marks:", average)

