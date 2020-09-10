#To sort a dict according to value

d=eval(input("Enter a dict( {key:value} )"))
l=[]
l1=[]
l2=[]
l3=[]
for x in d:
    l+=[d[x]]
    l1+=[x]

l2=sorted(l)

for e in l2:
    for x in d:
        if e==d[x]:
            l3.append(x)    # key is l3=[3,1,4,2] and value is l2=[A,B,C,D]
d1={}
j=0
for e in l3:
    while j<=len(l2):
        d1[e]=l2[j]
        j+=1
        break
	    
print("The sorted dict by value is",d1)	





    
