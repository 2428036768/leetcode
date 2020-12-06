def generate(numRows):
    ans=[]
    for i in range(numRows):
        row=[]
        for j in range(0,i+1):
            if j==0 or j==i:
                row.append(1)
            else:
                row.append(ans[i-1][j-1]+ans[i-1][j])
        ans.append(row)
    return ans

print(generate(5))