#TO find HCF of two numbers

def f(a,b,i):
    
    if a%i==0 and b%i==0:
        return i
    else:
        return f(a,b,i-1)

y,z=int(input("Enter first number")),int(input("Enter second number"))
x=f(y,z,min(y,z))
print("The HCF of the two numbers is",x)
