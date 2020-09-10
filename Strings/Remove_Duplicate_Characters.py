s=str(input("Enter any string: "))
s1=""
j=0
for e in s:
    if s.index(e)==j:
        s1+=e
    j+=1

print(s1)
