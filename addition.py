year=int(input("enter the number"))
for i in range(year):
    if i%4==0:
        print("leap year")
    else:
        print("not leap year")
    if i%100==0:
        print("leap year")
    else:
        print("not leap year")
    if i%400==0:
        print("leap year")
    else:
        print("not leap year")
    
    
