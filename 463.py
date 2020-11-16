a=[[1,1],[1,0],[0,0]]
print(len(a))
print(len(a[0]))


def judge(array,i,j):
    cnt=0
    if j-1<0 or array[i][j-1]==0: cnt+=1
    if j+1==len(array[0]) or array[i][j+1]==0: cnt+=1
    if i-1<0 or array[i-1][j]==0: cnt+=1
    if i+1==len(array) or array[i+1][j]==0: cnt+=1
    return cnt



ans=0

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]==1:
            ans+=judge(a,i,j)
        else:
            continue

print(ans)
        