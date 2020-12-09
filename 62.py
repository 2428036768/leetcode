dp = [[1]+[0] * (2-1) for _ in range(2-1)]   # [[1,0]]
print(dp)
dp = [[1]*2]+[[1]+[0] * (2-1) for _ in range(2-1)]    #[[1,1]]+[[1,0]]=[[1,1],[1,0]]
print(dp)
dp = [1]*2+[[1]+[0] * (2-1) for _ in range(3-1)]    #[[1,1]]+[[1,0]]=[[1,1],[1,0]]
print(dp)


"""
动态规划
中等
"""



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]