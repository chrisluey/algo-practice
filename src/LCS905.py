class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = acc = 0
        while i < len(nums) and acc < len(nums): 
            if nums[i] % 2 != 0:
                nums.append(nums[i])
                del nums[i]
            else:
                i += 1
            acc += 1
        return nums