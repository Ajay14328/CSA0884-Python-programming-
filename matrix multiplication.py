n=[[1,2],[3,2]]
m=[[2,3],[3,4]]
ans=[[0,0],[0,0]]
for i in range(len(n)):
    for j in range(len(m)):
        for k in range(len(ans)):
            ans[i][j]+=n[i][k]+m[k][i]
print(ans)
