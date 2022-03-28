class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = floor((lo + hi) / 2)
            if nums[mid] == target:
                return True
            while nums[lo] == nums[mid] and lo < mid:
                lo += 1
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi -= 1
                else:
                    lo += 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo += 1
                else:
                    hi -= 1       
        return False