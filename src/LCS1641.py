class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        dp = [1, 1, 1, 1, 1]
        n -= 1
        while n > 0:
            dp[4] += 1 + dp[1] + dp[2] + dp[3]
            dp[3] += 1 + dp[1] + dp[2]
            dp[2] += 1 + dp[1]
            dp[1] += 1
            n -= 1
        return sum(dp)