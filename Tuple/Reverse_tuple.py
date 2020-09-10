t=eval(input("Enter a tuple "))
t1=[]
t2=list(t)

for j in range(len(t)-1,0,-1):
        t1.append(t2[j])
t1.append(t2[0])
t=tuple(t1)
print(t)
