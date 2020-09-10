# Sum of digits of given numbers

def f(n):
    if n==0:
        return 0
    return n%10+f(n//10)
x=f(265)
print(x)
