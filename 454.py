"""
四数相加
中等
总结，看到形如：A+B....+N=0的式子，要转换为(A+...T)=-((T+1)...+N)再计算，这个T的分割点一般是一半，特殊情况下需要自行判断。定T是解题的关键。
空间换时间
"""



import collections

def fourSumCount(A,B,C,D):
    count=collections.Counter(a+b for a in A for b in B)   #生成a+b的哈希表

    ans=0
    for c in C:
        for d in D:
            if -c-d in count:
                ans+=count[-c-d]
    
    return ans


A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(fourSumCount(A,B,C,D))