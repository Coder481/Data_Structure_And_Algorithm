#Sum of cubes of first N natural numbers

def f(n):
    if n==1:
        return 1
    return n**3+f(n-1)
x=f(3)
print(x)
