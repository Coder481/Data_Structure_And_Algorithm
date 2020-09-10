#Reverse order of N odd natural numbers

def f(n):
    if n==1:
        print(n)
        return 1
    return print(2*n-1),f(n-1)
f(5)
