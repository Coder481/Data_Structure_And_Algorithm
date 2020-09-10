#To print first N even natural numbers

def f(i,n):
    if i<=n:
        print(2*i)
        f(i+1,n)
    
f(1,10)

