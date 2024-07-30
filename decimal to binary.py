def decimal_binary(n):
    if n==0:
        return 0
    binary=""
    while n>0:
        binary+=str(n%2)
        n=n//2
    return binary
n=4
print(decimal_binary(n))
