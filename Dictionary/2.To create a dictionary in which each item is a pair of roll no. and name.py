#To create a dictionary in which each item is a pair of roll no. and name

d={}
n=int(input("Enter number of students"))

for i in range(1,n+1):
    k=int(input("Enter roll number of %d student"%i))
    v=input("Enter name of %d student"%i)
    d[k]=v
print(d)
