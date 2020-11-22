"""
有效字母异位
简单
"""

def isAnagram(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

s = "rat"
t = "car"
print(isAnagram(s,t))