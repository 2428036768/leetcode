def maxProduct(nums):
    if not nums:
        return
    nums.sort(reverse=True)
    return (nums[0]-1)*(nums[1]-1)

nums = [3,4,5,7]
print(maxProduct(nums))