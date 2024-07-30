array="engineering"
vowles="AaEeIiOoUu"
v_count=0
c_count=0
for i in range(0,len(array)):
    if array[i] in (vowles):
        v_count+=1
    else:
        c_count+=1
print(v_count,c_count)
