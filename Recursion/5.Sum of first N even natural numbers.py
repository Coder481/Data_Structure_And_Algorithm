# Sum of first N even natural numbers

def f(n):
    if n==0:
        return 0
    return (2*n)+f(n-1)
x=f(3)
print(x)
