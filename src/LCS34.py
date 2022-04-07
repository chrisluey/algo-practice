class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        def search(lo: int, hi: int) -> List[int]:
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l, r = search(lo, mid), search(mid + 1, hi)
                if -1 in l:
                    return r
                elif -1 in r:
                    return l
                else:
                    return [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums) - 1)