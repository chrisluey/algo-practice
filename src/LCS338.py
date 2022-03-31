class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        if n == 0:
            return result
        result.append(1)
        if n == 1:
            return result
        curr = 0
        power = 2
        for i in range(2, n + 1):
            if curr == power:
                power = i
                result.append(1)
                curr = 1
            else:
                result.append(1 + result[curr])
                curr += 1
        
        return result