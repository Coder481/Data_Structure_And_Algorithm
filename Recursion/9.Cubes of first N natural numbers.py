#cubes of first N natural numbers

def f(i,n):
    if i<=n:
        print(i**3)
        f(i+1,n)
f(1,10)
