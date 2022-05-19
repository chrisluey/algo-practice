class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total, currTotal = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            currTotal += gas[i] - cost[i]
            if currTotal < 0:
                start = i + 1
                currTotal = 0
        if total < 0:
            return -1
        else:
            return start