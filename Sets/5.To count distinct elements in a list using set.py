#To count distinct elements in a list using set

l=eval(input("Enter list (In square braces)"))
s=set(l)
c=0
for e in s:
    c+=1

print(c)
