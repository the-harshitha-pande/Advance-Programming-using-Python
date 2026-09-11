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

