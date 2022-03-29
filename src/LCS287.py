class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            for i in nums:
                if mid >= i:
                    count += 1
            if count <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo