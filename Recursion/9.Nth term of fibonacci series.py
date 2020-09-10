#To find Nth term of fibonacci series

def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    p=f(n-1)+f(n-2)
    return p

z=int(input("Enter Nth term-"))
x=f(z)
print("The %dth term of fibonacci series is"%z,x)
