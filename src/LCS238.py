class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, oneZero, result = None, 0, []
        for i in nums:
            if i == 0:
                if oneZero == 0:
                    oneZero = 1
                else:
                    oneZero += 1
            else:
                if prod == None:
                    prod = i
                else:
                    prod *= i
        for i in nums:
            if i == 0:
                if oneZero == 1:
                    result.append(prod)
                else:
                    result.append(0)
            else:
                if oneZero == 0:
                    result.append(prod // i)
                else:
                    result.append(0)
        return result