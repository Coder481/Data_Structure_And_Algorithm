def LCM(a,b):
    for i in range(1,a*b+1):
       if i%a==0 and i%b==0:
        return i
        break

x,y=int(input("ENter first number ")),int(input("ENter second number "))
z=LCM(x,y)
print("LCM of",x," and",y," is",z)
