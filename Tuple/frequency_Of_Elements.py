t=eval(input("Enter a tuple(integers only)"))

for i in range(0,3):
    x=int(input("Enter the element to find frequency"))
    c=0
    for e in t:
        if e==x:
           c+=1

    print("The frequency of %d is "%x,c)
