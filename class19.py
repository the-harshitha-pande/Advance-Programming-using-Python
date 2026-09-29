#decoratores - also a function which modifies(adding) the behaviour of another function whth out changing basic functionality 
#wrapper - one userdefine function tht has multiple operations  

#conceptually
# original function
# decorator
# modified/enhanced function

#uppercase change
def casechange(function): #function passes as argument casechange is decorator
    def innerfun():
        return function().upper()
    return innerfun
@casechange
def message():
    return "Namah Shivaya"
print(message())

