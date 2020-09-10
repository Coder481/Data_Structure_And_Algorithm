#Reverse of cubes of first n natural numbers

def f(n):
    if n==1:
        return print(n**3)
    return print(n**3),f(n-1)
f(5)
