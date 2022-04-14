class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n, shift_num = len(grid), len(grid[0]), k
        if k >= m * n:
            shift_num %= m * n
        temp = [row[:] for row in grid]
        for i in range(m):
            for j in range(n):
                acc, y, x = shift_num, i, j
                while acc > 0:
                    if y == m - 1 and x == n - 1:
                        x, y = 0, 0
                    elif x == n - 1:
                        y += 1
                        x = 0
                    else:
                        x += 1
                    acc -= 1
                grid[y][x] = temp[i][j]
        return grid