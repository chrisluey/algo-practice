class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        curr = nums[0]
        acc = 0
        for i in range(1, len(nums)):
            if curr != nums[i]:
                acc += 1
                nums[acc] = nums[i]
                curr = nums[i]
        return acc + 1
            