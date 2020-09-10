t=eval(input("Enter a tuple(integer values) "))


for j in range(0,4):
    x=int(input("Enter any integer value to count:"))

    count=0
    for i in range(0,len(t)):
         if t[i]==x:
             count+=1

    print("Number of %d is"%x,count)
 


    
print("Total number of elements in the tuple is",len(t))
