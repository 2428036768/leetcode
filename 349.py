

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    if len(set1)>len(set2):             #判断集合中元素个数更少的那个，每个元素是否存在与大集合的交集
        ans=intersection_self(set2,set1)
    else:
        ans=intersection_self(set1,set2)
    return ans

def intersection_self(set1,set2):
    return [i for i in set1 if i in set2]





nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1,nums2))
