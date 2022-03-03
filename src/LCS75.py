class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        slow = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1
        for i in range(slow,len(nums)):
            if nums[i] == 1:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1