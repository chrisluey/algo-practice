class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        tuple_list, result = [], [""] * len(score)
        for i in range(len(score)):
            tuple_list.append((score[i], i))
        heapq.heapify(tuple_list)
        acc = len(tuple_list)
        while tuple_list:
            index = heapq.heappop(tuple_list)[1]
            if acc == 1:
                result[index] = "Gold Medal"
            elif acc == 2:
                result[index] = "Silver Medal"
            elif acc == 3:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(acc)
            acc -= 1
        return result