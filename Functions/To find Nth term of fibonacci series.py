#To find Nth term of fibonacci series(TSRS)

def f1(a):
     l=[1,1]
     i=2
     while True:
          l.append(l[i-1]+l[i-2])
          if i==a-1:
             break
          i+=1
     return l[a-1]

z=int(input("Enter nth term(n>2)-"))
x=f1(z)
print("The %dth term of fibonacci series is"%z,x)
