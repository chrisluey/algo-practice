class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def tryPermute(rem: List[int], curr: List[int]) -> None:
            if len(curr) == len(nums):
                result.append(curr)
                return
            else:
                for i in range(len(rem)):
                    list_copy = rem[:]
                    temp = list_copy.pop(i)
                    tryPermute(list_copy, curr+[temp])
        tryPermute(nums,[])
        return result