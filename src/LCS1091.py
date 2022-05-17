class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid) - 1]:
            return -1
        q =  deque()
        q.append((0, 0, 1))
        while len(q) > 0:
            curr = q.popleft()
            if curr[0] == len(grid) - 1 and curr[1] == len(grid) - 1:
                return curr[2]
            # print(curr[2])
            if  len(grid) > curr[0] - 1 >= 0 and len(grid) > curr[1] - 1 >= 0 and grid[curr[0] - 1][curr[1] - 1] != 1:
                grid[curr[0] - 1][curr[1] - 1] = 1
                q.append((curr[0] - 1, curr[1] - 1, curr[2] + 1))
            if len(grid) > curr[0] - 1 >= 0 and len(grid) > curr[1] >= 0 and grid[curr[0] - 1][curr[1]] != 1:
                grid[curr[0] - 1][curr[1]] = 1
                q.append((curr[0] - 1, curr[1], curr[2] + 1))
            if len(grid) > curr[0] - 1 >= 0 and len(grid) > curr[1] + 1 >= 0 and grid[curr[0] - 1][curr[1] + 1] != 1:
                grid[curr[0] - 1][curr[1] + 1] = 1
                q.append((curr[0] - 1, curr[1] + 1, curr[2] + 1))
            if len(grid) > curr[0] >= 0 and len(grid) > curr[1] - 1 >= 0 and grid[curr[0]][curr[1] - 1] != 1:
                grid[curr[0]][curr[1] - 1] = 1
                q.append((curr[0], curr[1] - 1, curr[2] + 1))
            if len(grid) > curr[0] >= 0 and len(grid) > curr[1] + 1 >= 0 and grid[curr[0]][curr[1] + 1] != 1:
                grid[curr[0]][curr[1] + 1] = 1
                q.append((curr[0], curr[1] + 1, curr[2] + 1))
            if len(grid) > curr[0] + 1 >= 0 and len(grid) > curr[1] - 1 >= 0 and grid[curr[0] + 1][curr[1] - 1] != 1:
                grid[curr[0] + 1][curr[1] - 1] = 1
                q.append((curr[0] + 1, curr[1] - 1, curr[2] + 1))
            if len(grid) > curr[0] + 1 >= 0 and len(grid) > curr[1] >= 0 and grid[curr[0] + 1][curr[1]] != 1:
                grid[curr[0] + 1][curr[1]] = 1
                q.append((curr[0] + 1, curr[1], curr[2] + 1))
            if len(grid) > curr[0] + 1 >= 0 and len(grid) > curr[1] + 1 >= 0 and grid[curr[0] + 1][curr[1] + 1] != 1:
                grid[curr[0] + 1][curr[1] + 1] = 1
                q.append((curr[0] + 1, curr[1] + 1, curr[2] + 1))
        return -1