def palindrome(s):
    return s==s[::-1]
s=str(input("enter th string="))
print(palindrome(s))
