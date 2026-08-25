def add(a, b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b==0:
        raise ValueError("denominator cannot be zero")
    return a/b