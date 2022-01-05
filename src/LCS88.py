class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = x = 0
        result = list(nums1)
        while i < m or j < n:
            if i >= m:
                nums1[x] = nums2[j]
                j += 1
            elif j >= n:
                nums1[x] = result[i]
                i += 1
            elif result[i] <= nums2[j]:
                nums1[x] = result[i]
                i += 1
            else:
                nums1[x] = nums2[j]
                j += 1
            x += 1