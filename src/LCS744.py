class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        lo, hi, result = 0, len(letters) - 1, len(letters) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if letters[mid] > target:
                if letters[mid] < letters[result]:
                    result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return letters[result]