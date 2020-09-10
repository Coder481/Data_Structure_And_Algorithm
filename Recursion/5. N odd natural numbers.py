#To print first N odd natural numbers

def f(i,n):
    if i<n:
        print(2*i+1)
        f(i+1,n)
f(0,5)
