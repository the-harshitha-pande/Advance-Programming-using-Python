#when does recurssive function fail and how would u handle that
#stack overflow.
#handle: dp->memoraization, traditional way is iterative approach, tail recurssive(the recurssive call is last thing function does)
#TAIL RECURSSION 
#recurssive tree:(ada: masters, substitution, recurssive tree,brute-force)
#factorial of number using recurssive tree:code
#factorial of number using tail recurssive :code
def factorial(n, result=1):
    if n == 0:
        return result
    return factorial(n-1, result * n)
print(factorial(10))
#factorial(5,1)
#factorial(4,5)
#factorial(3,20)
#factorial(2,60)
#factorial(1,120)
#factorial(0,120)
#120

#try to generate recurrent ans and display how we reach solution like tree only
def factorial(n, result=1):
    print(n,result)
    if n == 0:
        return result
    return factorial(n-1, result * n)
print(factorial(5))

#sum of n numbers using tail recurssion
def sum_numbers(n, result=0):
    if n==0:
        return result
    return sum_numbers(n-1,result+n)
print(sum_numbers(5))

#fibonaccie using tail recurssion
def fibona(n, a=0, b=1):
    if n==0 :
        return a
    return fibona(n-1,b,a+b)
n=int(input("enter the number of terms"))
for i in range(n):
    print(fibona(i), end = " ")


