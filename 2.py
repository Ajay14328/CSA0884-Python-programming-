n=int(input("enter the number"))
for i in range(n+1):
    for j in range(1,i+1):
        print(float(j//10),end=" ")
    print(" ")
