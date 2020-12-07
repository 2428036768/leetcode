"""
反转矩阵后的得分
中等
贪心
"""
def matrixScore(A):
    m=len(A)
    n=len(A[0])
    ret=m*2**(n-1)

    for i in range(1,n):
        num=0
        for j in range(m):
            if A[j][0]==1:
                num+=A[j][i]
            else:
                num+=(1-A[j][i])
        k=max(num,m-num)
        ret+=k*2**(n-i-1)
    
    return ret

A=[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(matrixScore(A))

