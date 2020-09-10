#To print sum of values of dictionary taken from keyboard

d=eval(input('Enter a dict( {key:value} )'))

s=str()
for e in d:
    s+=d[e]

print(s)
