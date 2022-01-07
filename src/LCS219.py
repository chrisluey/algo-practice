class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        this_dict = {}
        for i in range(len(nums)):
            other_val = this_dict.get(nums[i])
            if other_val == None:
                this_dict[nums[i]] = i
            elif abs(other_val - i) > k:
                this_dict[nums[i]] = i
            else:
                return True
        return False
                