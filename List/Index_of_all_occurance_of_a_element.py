l=[]
k=[]
n=int(input("Enter list length:"))
print("Enter elements of list:")
for i in range(0,n):
    ele=int(input())
    l.append(ele)
print("The given list is:")
print(l)
a=int(input("Enter the number to find index:"))

for i in range(0,n):
    if l[i]==a:
        print(i)
        k.append(i)

print("The list of indices of all occurance of %d is "%a,k)
