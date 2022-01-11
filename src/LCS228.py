class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0:
            return result
        start = prev = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] - 1 == prev:
                prev = nums[i]
            else:
                if start != prev:
                    result.append(str(start) + "->" + str(prev))
                    start = nums[i]
                    prev = nums[i]
                else:
                    result.append(str(start))
                    start = nums[i]
                    prev = nums[i]
        if start != prev:
            result.append(str(start) + "->" + str(prev))
        else:
            result.append(str(start))
        return result        
        