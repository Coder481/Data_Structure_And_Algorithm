#To create a power set

s1=eval(input("Enter a set(in curly braces)"))
p=list()
s=list(s1)
p1=list(s)

for e in s:
    p=p+[e]

    
p=p+p1+[]
print(p)

