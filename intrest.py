p=int(input("enter the amount="))
n=int(input("enter the no of years="))
sc=input("senior citizen(yes/no)")
g=input("gender (male/female)")
if sc=='y' and g=='m':
   print("si=",(p*n*12)/100)
elif sc=='y' and g=='f':
    print("si=",(p*n*15)/100)
else:
    print("si=",(p*n*10)/100)
