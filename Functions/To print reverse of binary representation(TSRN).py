#To print reverse of binary representation of a number

def f1(a):
    y=bin(a)
    x=y[2::]
    l=[]
    print("%d"%a,"->",x)
    for e in x:
        l.append(e)  
    
    print(l)
    l1=[] 
    for i in range(len(l)-1,0,-1):
        l1.append(l[i])
    l1.append(l[0])
    print(l1)
    b=''
    for e in l1:
        L=str(e)
        b+=L
    print("Reverse of bin repres. of %d is"%a,b)

z=int(input("Enter any number-"))
f1(z)
