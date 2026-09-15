#an online food-delivery 
class foodorder:
    def __init__(self, customer, item, quantity): #parameterised constructor
        self.customer=customer
        self.item=item
        self.quantity=quantity
order1=foodorder("anita","pizza",1)   #foororder() is the constructor
order2=foodorder("bharath","dosa",2)  #order 1 and order2- multiple

print("customer name:"+order1.customer)
print("food ordered:"+order1.item)
print("quantity:",order2.quantity)

#instance variable and normal variable difference - 
#any other builtin method other thn __init__ [string is also a builtin method with in a class to print the object ]
#encapsulation
# how do u make a variable private - prefixed with 2 underscores - acceced only by 