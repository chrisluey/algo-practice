class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        result, slow = 0, 1
        for i in range(1,len(nums) - 1):
            if nums[i] - nums[i-1] == nums[i + 1] - nums[i]:
                result += slow
                slow += 1
            else:
                slow = 1
        return result