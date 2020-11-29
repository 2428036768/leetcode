"""
三角形的最大周长
简单
"""
def largestPerimeter(A):
    if not A: return 0
    A.sort(reverse=True)

    for i in range(len(A)-2):
        if A[i]<A[i+1]+A[i+2]:
            return A[i]+A[i+1]+A[i+2]
    return 0
A=[2,1,1]
print(largestPerimeter(A))
    
