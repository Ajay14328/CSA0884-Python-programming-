n=int(input("number="))
total=0
for i in range(1,n):
    if n%i==0:
        total=total+i
if total==n:
    print("it is a perfect number")
else:
    print("not a perfect number")
        
