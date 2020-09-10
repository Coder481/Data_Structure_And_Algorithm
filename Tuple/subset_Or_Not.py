t1=eval(input("Enter first tuple(integer values)"))
t2=eval(input("Enter second tuple(integer values)"))
c1=0
c2=0

for e in t2:
    for i in range(len(t1)):
        if e==t1[i]:
            c1+=1
            break
        elif e!=t1[i]:
            continue

for e in t1:
    for i in range(len(t2)):
        if e==t2[i]:
            c2+=1
            break
        elif e!=t2[i]:
            continue


if c1==len(t2) and c2!=len(t1):
    print("second tuple is a subset of first tuple \n but first isn't a subset of second")
elif c2==len(t1) and c1!=len(t2):
    print("First tuple is a subset of second tuple \n but second  isn't a subset of first")
elif c1!=len(t2) and c2!=len(t1):
    print("No any tuple is a subset of other")
else:
    print("Both the tuples are subset of each other")
