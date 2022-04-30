class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        matrix = collections.defaultdict(list)
        
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                matrix[i].append((abs(x1 - points[j][0]) + abs(y1 - points[j][1]), j))
                matrix[j].append((abs(x1 - points[j][0]) + abs(y1 - points[j][1]), i))
        
        acc, result, visited, heap = 1, 0, [0] * len(points), matrix[0]
        visited[0] = 1
        heapq.heapify(heap)
        
        while heap:
            dist, v = heapq.heappop(heap)
            if not visited[v]:
                visited[v], acc, result = 1, acc + 1, result + dist
                for stuff in matrix[v]: heapq.heappush(heap, stuff)
            if acc >= len(points):
                break
        return result