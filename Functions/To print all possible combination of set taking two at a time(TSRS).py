#To find all possible combination of a set taking two elements at a time(TSRS)


def f1(a):
    b=a.copy()
    l=[]
    for i in a:
        for j in b:
            if i!=j:
               l.append({i,j})

    return l

s=eval(input("Enter a set( {int values} )"))
x=f1(s)
print(x)
