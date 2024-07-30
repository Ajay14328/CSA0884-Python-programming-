n=str(input("enter the string"))
vowles="aAEeIiOoUu"
v=[]
c=[]
for i in range(len(n)):
    if n[i] in vowles:
        v.append(n[i])
    else:
        c.append(n[i])
print(c,v)

