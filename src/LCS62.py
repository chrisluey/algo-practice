class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        # result = 0
        if m == 1 or n == 1:
            return 1
        result = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(0,n):
            result[i][0] = 1
        for j in range(0,m):
            result[0][j] = 1
        for i in range(1,n):
            for j in range(1,m):
                result[i][j] = result[i-1][j] + result[i][j-1]
        
        return result[-1][-1]
        