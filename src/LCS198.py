class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        curr = nums[0]
        if len(nums) == 1:
            return curr
        prev = curr
        curr = max(nums[1], prev)
        for i in range(2, len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)
        return curr
            