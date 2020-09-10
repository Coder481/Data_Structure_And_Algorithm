t=eval(input("Enter first tuple(integer values) "))
l=list(t)

for i in range(1,len(t)):
    if l[0]>=l[i]:
        continue
    elif l[0]<l[i]:
        l[0]=l[i]

print("Greatest element in the tuple is ",l[0])
