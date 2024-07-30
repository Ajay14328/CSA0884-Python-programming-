n=[[1,2],[2,3]]
m=[[3,2],[4,3]]
ans=[[0,0],[0,0]]
for i in range(len(n)):
    for j in range(len(m)):
        ans[i][j]=n[i][j]+m[i][j]
print(ans)
