#To produce sample space to get a sum of dice values ,when rolled,  n

s1={1,2,3,4,5,6}
s2={1,2,3,4,5,6}
n=int(input("Enter any value n (0<n<12)"))
s3=set()

    
for e in s1:
    for x in s2:
        if e+x==n:
            s3.add((e,x))
if 0<n<=12:
    print(s3)
else:
  print("Enter correct value of n")
