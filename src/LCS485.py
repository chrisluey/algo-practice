class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result, curr = 0, 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                result = max(result, curr)
                curr = 0
        return max(result, curr)