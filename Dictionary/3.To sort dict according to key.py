#To sort a dictionary according to key

d=eval(input("Enter a dict( {key:value} )"))
l=[]
for x in d:
    l=l+[x]

l.sort()
d1={}
for e in l:
    d1[e]=d[e]

print(d1)
