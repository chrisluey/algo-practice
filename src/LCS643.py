class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = curr = sum(nums[:k])
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            result = max(result, curr)
        return result / k