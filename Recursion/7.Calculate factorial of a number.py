#Calculate factorial of a number

def f(n):
    if n==1:
        return 1
    return n*f(n-1)
x=f(4)
print(x)
