def addition(m):
    if m==0:
        return 0
    else:
        return m+addition(m-1)
print(addition(3))
