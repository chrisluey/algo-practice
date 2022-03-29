class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        this_dict = {}
        for i in nums:
            if i in this_dict:
                this_dict[i] += i
            else:
                this_dict[i] = i
        prevKey, prev, curr = 0, 0, 0
        for key, value in this_dict.items():
            if prevKey == key - 1:
                prev, curr = curr, max(prev + value, curr)
            else:
                prev, curr = curr, curr + value
            prevKey = key
        return curr