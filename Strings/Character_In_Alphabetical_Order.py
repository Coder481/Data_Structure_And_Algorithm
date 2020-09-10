
s1="abcdefghijklmnopqrstuvwxyz"
s2=s1.upper()
s=str(input("Enter any string: "))
for i in range(0,len(s1)):
    for j in range(0,len(s)):
        if s1[i]==s[j]:
            print(s[j])
        elif s2[i]==s[j]:
            print(s[j])
