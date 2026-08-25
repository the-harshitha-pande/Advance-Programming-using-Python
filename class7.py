#what are modules- can be grp of task can be function variable does a particular task .module is specific task collection is package
# collection of such library tht perform particular task also called as library or package,-not necessary it always to be function
#ex:calculator.py 
#used bcz
#code reuseability
#
# easy

#availabel modules
#different modules list 

#import statement - there are several ways

#import entire module
"""import math
print(math.sqrt(5))
print(math.pi)

#import specific function
from math import sqrt
print(sqrt(5))

#multiple methods import
from math import sqrt, factorial

#import using alias
import math as m
print(m.sqrt(9))
print(m.pi)"""

#wt is library and package(a package is a directory containing related python modules, collection of modules like numpy(array,list),math:under math different modules r present) list some library n package
# how can you create a user defined module(with extenshion of .py), how would u save a module , create a module airthematic operations(functions defined to module)
# (how would u save and utilise user defined module-list all the ways(1.import module_name,2.from module_name import method1name,method2name,
# 3.import modulename as alias_name))

#university
#**_init_.py -
#**student.py
#********stu_details()-methods
#********stu_search.py-sub module


#how would you create a package- create a directory(folder) , 3 main functions ..
#why matplotlib,tensorflow is package not module why?
#know about init(Acts as user defined must hv this module which will allow access to all other module within when python version is less then 3.3, now it )

#create package,create project folder,in open in vscode (in jupyter other way )


#creating module called calculator
#1.
import calculator

print("sum:",calculator.add(10,20))
print("difference:",calculator.subract(10,20))
print("product:",calculator.multiply(10,20))
print("quotient:",calculator.divide(10,20))

#2.
from calculator import add,subract,multiply,divide
print(add(3,4))
print(subract(3,4))
print(multiply(3,4))
print(divide(3,4))

#3.
import calculator as c
print("sum:",c.add(10,20))
print("difference:",c.subract(10,20))
print("product:",c.multiply(10,20))
print("quotient:",c.divide(10,20))

