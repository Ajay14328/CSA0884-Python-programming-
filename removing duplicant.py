array=[1,5,10,5,1,2,3]
answer=[]
for i in array:
    if i not in answer:
       answer.append(i)
print(answer)
