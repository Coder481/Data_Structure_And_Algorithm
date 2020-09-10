#To calculate sum of all odds and sum of all evens in a list(TSRS)

def f1(l):
    E=0
    O=0
    for e in l:
        if e%2==0:
            E+=e
        elif e%2!=0:
            O+=e
    return O,E
z=eval(input("Enter a list( [int values] )"))
x=f1(z)

print("Sum of odd and Sum of even numbers is respec.",x)
