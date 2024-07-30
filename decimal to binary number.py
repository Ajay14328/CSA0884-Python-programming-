def decimal_to_binary(n):
    if n==0:
        return 0
    binary=""
    while n>0:
        binary+=str(n%2)
        n=n//2
    return binary
n=int(input("enter the number="))
binary_num=decimal_to_binary(n)
print("binary_number=",binary_num)
