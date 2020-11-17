"""
桶排序
list.append()是追加到末尾   [1,2,3].append([4,5])=[1,2,3,[4,5]]
list.extend()扩展到末尾     [1,2,3].extend([4,5])=[1,2,3,4,5]
"""

import collections
def allCellsDistOrder(R,C,r0,c0):
    maxDist=max(r0,R-r0-1)+max(c0,C-c0-1)
    buket=collections.defaultdict(list)
    dist = lambda r,c,r0,c0 : abs(r-r0)+abs(c-c0)

    for i in range(R):
        for j in range(C):
            buket[dist(i,j,r0,c0)].append([i,j])

    ans=[]
    for i in range(maxDist+1):
        ans.extend(buket[i])
    print(ans)

allCellsDistOrder(2,2,0,1)
