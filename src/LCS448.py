class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        this_list = set(range(1,len(nums) + 1))
        for i in nums:
            this_list.discard(i)
        return list(this_list)