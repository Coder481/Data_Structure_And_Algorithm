#To create a set of first n prime numbers

n=int(input("Enter how many prime numbers do want"))

c=0
s=set()
i=2
while True:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        c+=1
        s.add(i)
    if c==n:
        break
    i+=1
            
print(s)
