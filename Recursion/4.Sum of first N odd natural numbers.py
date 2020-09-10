# Sum of first N odd natural numbers

def f(n):
    if n==1:
        return 1
    return (2*n-1)+f(n-1)
x=f(5)
print(x)
