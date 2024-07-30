n=int(input("enter the number="))
m=int(input("enter the number="))
d=max(n,m)
v=[]
for i in range(2,d):
    if n%i and m%i==0:
        v.append(i)
print(v)
hcf=max(v)
lcm=(n*m)/hcf
gcd=(n*m)/lcm
print(lcm,gcd)
