class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # result.append([])
        def trySubset(curr: List[int], rem: List[int]) -> None:
            result.append(curr)
            if len(rem) == 0:
                return
            else:
                list_copy = rem[:]
                for i in range(len(rem)):
                    
                    trySubset(curr+[rem[i]], list_copy[i+1:])
        trySubset([],nums)
        return result