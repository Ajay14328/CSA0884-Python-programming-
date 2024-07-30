def frequency_count(array):
    n={}
    for i in array:
        if i in n:
            n[i]=n[i]+1
        else:
            n[i]=1
    return n
array=[1,1,1,1,1,2,2,2,3,3,3,4,4,4]
print(frequency_count(array))
