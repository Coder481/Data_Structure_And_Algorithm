#To check whether a set is a subset of another or not

s1=eval(input("Enter first set(in curly braces)"))
s2=eval(input("Enter second set(in curly braces)"))

c1=0
c2=0
for e in s2:
    for x in s1:
        if e==x:
            c1+=1
            break
        elif e!=x:
            continue

for e in s1:
    for x in s2:
        if e==x:
            c2+=1
            break
        elif e!=x:
            continue

if c1==len(s2) and c2!=len(s1):
    print("s2 is a subset of s1 but s1 is not subset of s2")
if c1!=len(s2) and c2==len(s1):
    print("s2 isn't a subset of s1 but s1 is a subset of s2")
if c1==len(s2) and c2==len(s1):
    print("both are subsets of each other")
if c1!=len(s2) and c2!=len(s1):
    print("None of them are subset of other")
    
