class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        nums.sort()
        for i in range(size):
            if i != nums[i]:
                return i
        return size