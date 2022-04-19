class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result, m, n = 0, len(matrix), len(matrix[0])
        dp = [[0 for x in range(n + 1)] for j in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    curr = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    dp[i + 1][j + 1] = curr
                    result = max(curr, result)
        return result**2    