"""
转置矩阵
简单：尺寸为 R x C 的矩阵 A 转置后会得到尺寸为 C x R 的矩阵 ans，对此有 ans[c][r] = A[r][c]。
"""
def transpose(A):
    if not A:
        return
    R=len(A)
    C=len(A[0])
    ans=[[0]*R for _ in range(C)]
    for i in range(R):
        for j in range(C):
            ans[j][i]=A[i][j]
    print(ans)

A=[[1,2,3],[4,5,6]]
transpose(A)
            
