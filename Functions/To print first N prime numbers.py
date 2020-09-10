#Print first N prime numbers(TSRN)

def f1(a):
    count=0
    x=1
    while True:
        x+=1
        for i in range(2,x):
            if x%i==0:
               break
        else:
          count+=1
          print(x)    
           
        if count==n:
           break

n=int(input("Enter how many prime numbers do you want to print: "))
f1(n)
