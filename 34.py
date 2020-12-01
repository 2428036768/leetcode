"""
中等
在排序数组中查找元素的第一个和最后一个位置
折半查找
"""
import math

def searchRange(nums,target):
    leftAns=binarySearch(nums,target,True)
    rightAns=binarySearch(nums,target,False)-1
    print(leftAns)
    print(rightAns)
    if leftAns<=rightAns and rightAns<len(nums) and nums[leftAns]==target and nums[rightAns]==target:
        return [leftAns,rightAns]
    else:
        return [-1,-1]

def binarySearch(nums,target,lower):
    right=len(nums)-1
    left=0
    ans=len(ans)
    while left<=right:
        mid=int((right+left)/2)
        if target<nums[mid] or (target<=nums[mid] and lower):
            right=mid-1
            ans=mid
        else:
            left=mid+1
    return ans
        
nums = [1]
target = 1
print(searchRange(nums,target))
    
        
