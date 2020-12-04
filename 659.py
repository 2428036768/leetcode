"""
分割数组为连续子序列
中等
"""
import collections
import heapq

def isPossible(nums):
    mp = collections.defaultdict(list)
    for x in nums:
        if queue := mp.get(x - 1):
            prevLength = heapq.heappop(queue)
            heapq.heappush(mp[x], prevLength + 1)
        else:
            heapq.heappush(mp[x], 1)
    
    return not any(queue and queue[0] < 3 for queue in mp.values())

nums=[1,2,3,3,4,5]
print(isPossible(nums))