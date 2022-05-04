class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        this_dict, result = collections.Counter(), 0
        for i in nums:
            if this_dict[i] > 0:
                this_dict[i] -= 1
                result += 1
            else:
                if k > i:
                    this_dict[k-i] += 1
        return result