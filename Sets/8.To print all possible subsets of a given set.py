#To print a all possible subsets of r elements from a given set of n elements

s1=eval(input("Enter a set(in curly braces)"))
s2=set()
s2=s1.copy()
s3=set()

for e in s1:
    for x in s2:
        
            s3.add((e,x))
print("The list subsets of length 2 is:\n",s3)



