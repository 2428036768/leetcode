"""
最大间距
基数排序
困难
"""

def maximumGap(nums):
    if len(nums)<2:
        return 0
    digit=len(str(max(nums)))   #求列表中最大数的位数
    
    for k in range(digit):         #从低位到高位，分别对数据进行排序
        buket=[[] for i in range(10)]
        for num in nums:
            buket[num//10**k%10].append(num) #按照每位的数字，进行分桶
        
        nums=[j for i in buket for j in i]   #将分桶排序完的数据重新组成链表

    gap=0
    for i in range(len(nums)-1):    #求出两个数之间最大gap
        gap=max(nums[i+1]-nums[i],gap)
    return gap
        


nums=[3,6,9,1]
print(maximumGap(nums))

