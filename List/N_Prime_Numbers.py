l=[]
n=int(input("Enter how many prime numbers do you want to print:"))
x=1
count=0
while True:
     x+=1
     for i in range(2,x):
         if x%i==0:
             break
     else:
      count+=1
      l.append(x)   

     if count==n:
         break

print(l)
