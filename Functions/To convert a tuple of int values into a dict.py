#To convert a tuple of int values in dict

def f1(a):
       d={}
       s=set(t)
       for e in s:
           d[e]=t.count(e)
       return d
    
t=eval(input("Enter a tuple( [int values] )"))
x=f1(t)
print(x)
