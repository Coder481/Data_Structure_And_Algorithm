s=str(input("Enter any string: "))
s1=s[len(s)::-1]
for i in range(0,len(s)):
    if s[i]!=s1[i]:
        print("%s is not palindrome string"%s)
        break
    else:
        print("%s is palindrome string"%s)
        break
