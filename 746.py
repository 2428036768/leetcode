"""
使用最小花费爬楼梯
动态规划
"""
def  minCostClimbingStairs(cost):
    """
    
    """
    dp=[0]*(len(cost)+1)
    for i in range(2,len(cost)+1):
        dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    
    return dp[-1]

cost = [10, 15, 20]
print(minCostClimbingStairs(cost))
