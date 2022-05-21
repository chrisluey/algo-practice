class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = [[0 for x in range(len(obstacleGrid[0]) + 1)] for y in range(len(obstacleGrid) + 1)]
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 1:
                        return 0
                    else:
                        grid[i + 1][j + 1] = 1
                elif obstacleGrid[i][j] == 1:
                    continue
                else:
                    grid[i + 1][j + 1] = grid[i][j + 1] + grid[i + 1][j]
        return grid[len(grid) - 1][len(grid[0]) - 1]