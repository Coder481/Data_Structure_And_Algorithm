#Sum of squares of first N natural numbers

def f(n):
    if n==1:
        return 1
    return n**2+f(n-1)
x=f(3)
print(x)
