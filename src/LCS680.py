class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        def checkThis(left: int, right: int, st: str) -> bool:
            while left < right:
                if st[left] == st[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return checkThis(l + 1, r, s) or checkThis(l, r - 1, s)
        return True