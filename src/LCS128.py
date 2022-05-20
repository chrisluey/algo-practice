class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        this_dict = defaultdict(int)
        result = 0
        for i in nums:
            if this_dict[i] != 0:
                continue
            if this_dict[i - 1] == 0 and this_dict[i + 1] == 0:
                this_dict[i] = (i, i, 1)
                result = max(result, 1)
            elif this_dict[i - 1] == 0:
                late = this_dict[i + 1]
                val = late[2] + 1
                this_dict[i] = (i, late[1], val)
                this_dict[late[1]] = (i, late[1], val)
                result = max(result, val)
            elif this_dict[i + 1] == 0:
                prev = this_dict[i - 1]
                val = prev[2] + 1
                this_dict[i] = (prev[0], i, val)
                this_dict[prev[0]] = (prev[0], i, val)
                result = max(result, val)
            else:
                prev = this_dict[i - 1]
                late = this_dict[i + 1]
                val = prev[2] + late[2] + 1
                this_dict[i] = (prev[0], late[1], val)
                this_dict[prev[0]] = (prev[0], late[1], val)
                this_dict[late[1]] = (prev[0], late[1], val)
                result = max(result, val)
        return result