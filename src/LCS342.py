class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def recurse(i: int) -> bool:
            if i == 1:
                return True
            if i % 4 != 0 or i == 0:
                return False
            return recurse(i // 4)
        return recurse(n)