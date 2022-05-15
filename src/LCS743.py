class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        this_dict = {}
        for i in times:
            if i[0] in this_dict:
                this_dict[i[0]].append((i[2], i[1]))
            else:
                this_dict[i[0]] = [(i[2], i[1])]
        visited, heap, visited[k-1] = [10**4] * n, [], 0
        heapq.heappush(heap, (0, k))
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            if curr[1] not in this_dict:
                continue
            for j in this_dict[curr[1]]:
                if visited[j[1] - 1] > curr[0] + j[0]:
                    visited[j[1] - 1] = curr[0] + j[0]
                    heapq.heappush(heap, (curr[0] + j[0], j[1]))
        result = max(visited)
        if result == 10**4:
            return -1
        else:
            return result