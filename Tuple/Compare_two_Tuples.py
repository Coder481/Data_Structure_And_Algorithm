t1=eval(input("Enter first tuple(integer values) "))
t2=eval(input("Enter second tuple(integer values) "))

c1=0
c2=0
j=0
for i in range(0,len(t1)):
    while j<len(t2):
        
        if t1[i]<t2[j]:
            print("First tuple is smaller and second is greater")
            c1+=1
            break
        
        elif t1[i]>t2[j]:
           print("First tuple is greater and second is smaller")
           c2+=1
           break
        
        else:
            j+=1
            break
    if c1==1 or c2==1:
        break
        
if c1!=1 and c2!=1:
    print("Both tuples are same")
