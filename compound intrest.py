p=int(input("enter the amount"))
t=int(input("enter the time in months"))
r=int(input("enter the intrest rate"))
ci=((p*(1+r/100)**t)-p)
print(ci)