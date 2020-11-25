"""
上升下降字符串
简单
桶排序
"""
def sortString(s):
    nums=[0]*26
    for char in s:
        nums[ord(char)-ord('a')]+=1
    
    ans=[]
    L=len(s)
    while L>0:
        for j in range(len(nums)):
            if nums[j]!=0:
                ans.append(chr(ord('a')+j))
                nums[j]-=1
                L-=1
        print(ans)
        for j in range(25,-1,-1):
            if nums[j]!=0:
                ans.append(chr(ord('a')+j))
                nums[j]-=1
                L-=1
        print(ans)
    print("".join(ans))

s='aaabbbccc'
sortString(s)