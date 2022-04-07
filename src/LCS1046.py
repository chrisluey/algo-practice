import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        invertedStones = [-x for x in stones]
        heapq.heapify(invertedStones)
        while len(invertedStones) >= 2:
            first = heapq.heappop(invertedStones)
            second = heapq.heappop(invertedStones)
            diff = first - second
            if diff != 0:
                heapq.heappush(invertedStones, diff)
        if len(invertedStones) == 1:
            return -invertedStones[0]
        else:
            return 0