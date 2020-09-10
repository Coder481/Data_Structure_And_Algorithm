#To calculate sum of first N natural numbers

def f(n):
    if n==1:
        return 1
    return n+f(n-1)
x=f(10)
print(x)
