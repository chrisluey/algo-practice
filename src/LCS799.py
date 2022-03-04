class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for x in range(query_row + 1)] for y in range(query_row + 1)]
        if poured == 0:
            return float(0)
        dp[0][0] = float(poured)
        for y in range(1,query_row + 1):
            for x in range(y + 1):
                if x > 0 and dp[y-1][x-1] > 1:
                    dp[y][x] += (dp[y-1][x - 1] - 1) / 2
                if x < y and dp[y-1][x] > 1:
                    dp[y][x] += (dp[y-1][x] - 1) / 2
        if  dp[query_row][query_glass] > 1:
            return float(1)
        else:
            return dp[query_row][query_glass]
                