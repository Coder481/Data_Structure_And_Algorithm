#To find cartesianproduct of two sets

s1=eval(input("Enter first set(in curly braces)"))
s2=eval(input("Enter second set(in curly braces)"))

s3=set()
for e in s1:
    for x in s2:
        s3.add((e,x))

print("The cartesian product of two sets is:\n",s3)
