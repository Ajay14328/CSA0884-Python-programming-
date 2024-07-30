n=[1,2,3,4,5,6,7,7,7,8]
m=len(n)
mean=sum(n)/m
print(mean)
if m%2==0:
    m1=n[m//2]
    m2=n[m//2-1]
    median=(m1+m2)/2
else:
    median=n[m//2]
print(median)
mode=max(n,key=n.count)
print(mode)
