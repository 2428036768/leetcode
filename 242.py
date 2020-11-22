"""
有效字母异位
简单
复杂度：排序的时间复杂度为 O(nlogn)，比较两个字符串是否相等时间复杂度为 O(n)，因此总体时间复杂度为 O(nlogn+n)=O(nlogn)。
"""

def isAnagram(s, t):
    return sorted(s) == sorted(t)

s = "rat"
t = "car"
print(isAnagram(s,t))