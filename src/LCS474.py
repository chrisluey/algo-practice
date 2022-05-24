class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(size + 1)]
        for i in range(1, size + 1):
            zeros = strs[i - 1].count("0")
            ones = len(strs[i - 1]) - zeros
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i - 1][j][k], 1 + dp[i - 1][j - zeros][k - ones])
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[size][m][n]