"""
记数质数
遍历法（根号） O(nlogn)
埃氏法 O(nloglogn)
"""

def  countPrimes(n):
    isPrimes=[1]*n
    ans=0
    for i in range(2,n):
        if isPrimes[i]:
            ans+=1
            for j in range(i,n):
                if i*j>=n:
                    break
                isPrimes[i*j]=0
    print(ans)

countPrimes(1)