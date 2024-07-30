n=[[1,3],[1,4]]
ans=[[0,0],[0,0]]
for i in range(len(n)):
    for j in range(len(ans)):
        ans[i][j]=n[j][i]
print(ans)
