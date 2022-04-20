class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    result[i] = max(result[j] + 1, result[i])
        return max(result)