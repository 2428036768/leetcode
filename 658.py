"""
找到K个最接近的元素
中等
"""
#方法一：我们可以将数组中的元素按照与目标 x 的差的绝对值排序，排好序后前 k 个元素就是我们需要的答案。
def findClosestElements(arr,k,x):
    if not arr:
        return 
    arr.sort(key=lambda a: abs(a-x))

    return sorted(arr[0:k])

arr=[1,2,3,4,5]
k=3
x=4
findClosestElements(arr,k,x)
#使用二分查找不断缩小所需数字范围