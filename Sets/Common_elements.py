s1=eval(input("Enter first set(In curly braces)"))
s2=eval(input("Enter second set(In curly braces)"))
l=set()
for e in s1:
    for x in s2:
        if e==x:
            l.add(e)
print("A set of coomon elements is",l)
