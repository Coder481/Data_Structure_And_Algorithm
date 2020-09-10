#Squares of first N natural numbers

def f(i,n):
    if i<=n:
        print(i**2)
        f(i+1,n)
f(1,10)
