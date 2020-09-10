#Reverse of squares of first n natural numbers

def f(n):
    if n==1:
        return print(n**2)
    return print(n**2),f(n-1)
f(5)
