t=eval(input("Enter a tuple(all type of values) "))
l1=[]
l2=[]
l3=[]
l4=[]

for e in t:
    if type(e)==int:
        l1.append(e)
    elif type(e)==str:
        l2.append(e)
    elif type(e)==float:
        l3.append(e)
    elif type(e)== complex:
        l4.append(e)

t1=tuple(l1)
t2=tuple(l2)
t3=tuple(l3)
t4=tuple(l4)


print("Tuple with homogenous elements ")
print(t1)
print(t2)
print(t3)
print(t4)
