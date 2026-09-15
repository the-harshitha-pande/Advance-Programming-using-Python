#polymorphism

'''
Polymorphism
Meaning "many forms," it lets a single interface, method, or object behave
differently depending on the context or the type of object acting on it.
'''

class EmailNotification:
    def send(self):
        print("Sending email notification")

class SMSNotification:
    def send(self):
        print("Sending SMS notification")

class PushNotification:
    def send(self):
        print("Sending push notification")

# one object invoking multiple constructors
notifications = [EmailNotification(), SMSNotification(), PushNotification()]  

for notification in notifications:
    notification.send()


#inheritance- 
# 1. properties and method duplication
# getting over the duplication 
#with in parenthesis with childclass we cal parent
# 2. only properties are inherited method is duplicated
#with help of looping we traverse the code 
#3. how to completely inherit properties and methods and have exclusive methods - super method

# magic method- string, Init     
# how magic methods can be differenciated from normal methods
# other name to magic method- dunder method(because it has double underscore)

#operator overloading - through magic methods
#airthemetic operators- operator || magic method 

#example- scenario of financial system for single class performing operator overloading

# when we hv 2 parameters the (self, other) self handles left hand and other handles right hand - since we hv to perform airthemetic oprators we need to pass
# operators - to pass to left operand the vale- self , other for passing value to right operand 
# then we call constructor 
# we hv 2 objects 
# then we perform addition of 2 obj 
# add method is automitacally invoked and balance gets updated and return variable total
# but here its single class performing operator overloading

# scenario of student - how to perform oprating overloading to multiple class

# __lt__  - magic method
# operator overloading,class/method overriding


#Inheritance

# single inheritance - object will be created for child class, and access paernt from child class
# multilevel inheritance- one parent - nxt class1 derive from parent then class2 derives from class1
# multiple -
#herarchy -one parent class multiple child class 
#hybrid- combination of any of 4 types above



