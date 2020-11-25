"""
    简单：移动零
    双指针
    """


def moveZeroes(nums):
    left = 0
    right = 1
    while right < len(nums):  # 控制右指针
        if nums[right]==0:
            right+=1
            continue
        while left < right:
            if nums[left] == 0:
                nums[left],nums[right]=nums[right],nums[left]
                break
            left+=1
        right+=1
    return nums

print(moveZeroes( [0,3,12]))


#官方题解
    # def moveZeroes(self, nums: List[int]) -> None:
    #     n = len(nums)
    #     left = right = 0
    #     while right < n:
    #         if nums[right] != 0:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #         right += 1
        