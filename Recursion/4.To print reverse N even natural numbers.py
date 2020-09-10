#To print reverse first n even natural numbers

def f(n):
    if n==0:
        return 0
    return print(2*n),f(n-1)
f(5)
