n=int(input("enter the number"))
sum=0
num=n
while num>0:
    digit=num%10
    sum+=digit**3
    num=num//10
if sum==n:
   print("it is an armstrong")
else:
    print("not an armstrong")
