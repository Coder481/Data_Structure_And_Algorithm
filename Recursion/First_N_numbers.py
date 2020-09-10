def f1(n):
    if n==1:
        print(n)
    a=f1(n-1)+1
    print(a)
ipt=int(input('Enter value of N:'))
f1(ipt)
