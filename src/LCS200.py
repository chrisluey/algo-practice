class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        def addNeighbors(x: int, y: int, grid: List[List[str]], queue: List[tuple]) -> None:
            if x - 1 >= 0 and grid[x - 1][y] != "*":
                queue.append((x - 1, y))
            if x + 1 < len(grid) and grid[x + 1][y] != "*":
                queue.append((x + 1, y))
            if y - 1 >= 0 and grid[x][y - 1] != "*":
                queue.append((x, y - 1))
            if y + 1 < len(grid[0]) and grid[x][y + 1] != "*":
                queue.append((x, y + 1))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1":
                    result += 1
                    grid[i][j] = "*"
                    q = []
                    addNeighbors(i, j, grid, q)
                    while len(q) > 0:
                        curr = q.pop()
                        if grid[curr[0]][curr[1]] == "1":
                            addNeighbors(curr[0], curr[1], grid, q)
                        grid[curr[0]][curr[1]] = "*"
                else:
                    grid[i][j] = "*"
        return result