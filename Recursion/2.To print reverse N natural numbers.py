#To print first n natural numbers in reverse order

def f(n):
    if n==1:
        return print(n)
    return print(n),f(n-1)
f(10)
