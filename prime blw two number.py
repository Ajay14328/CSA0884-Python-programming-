n=int(input("enter the number="))
m=int(input("enter the number="))
for i in range(n,m+1):
    for x in range(2,i):
        if i%x == 0:
            break
        else:
           print(i)
           break
