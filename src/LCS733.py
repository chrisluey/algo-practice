class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        def addValidNeighbors(this_q: List[tuple], this_visited: List[tuple], pixel: tuple, m: int, n: int) -> None:
            if pixel[0] - 1 >= 0 and (pixel[0] - 1, pixel[1]) not in this_visited:
                this_q.append((pixel[0] - 1, pixel[1]))
            if pixel[0] + 1 < m and (pixel[0] + 1, pixel[1]) not in this_visited:
                this_q.append((pixel[0] + 1, pixel[1]))
            if pixel[1] - 1 >= 0 and (pixel[0],  pixel[1] - 1) not in this_visited:
                this_q.append((pixel[0], pixel[1] - 1))
            if pixel[1] + 1 < n and (pixel[0], pixel[1] + 1) not in this_visited:
                this_q.append((pixel[0], pixel[1] + 1))
        
        
        color, m, n = image[sr][sc], len(image), len(image[0])
        visited, queue = [], []
        image[sr][sc] = newColor
        addValidNeighbors(queue, visited, (sr, sc), m, n)
        while len(queue) > 0:
            curr = queue.pop(len(queue) - 1)
            
            if image[curr[0]][curr[1]] == color:
                addValidNeighbors(queue, visited, curr, m, n)
                image[curr[0]][curr[1]] = newColor
            
            visited.append(curr)
        
    
        
        return image
        