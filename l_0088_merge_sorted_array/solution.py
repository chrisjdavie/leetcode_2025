from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_end: int = m - 1
        nums2_end: int = n - 1

        for i in range(m + n - 1, -1, -1):
            if nums2_end < 0:
                break
            if nums1_end < 0 or nums1[nums1_end] < nums2[nums2_end]:
                nums1[i] = nums2[nums2_end]
                nums2_end -= 1
            else:
                nums1[i] = nums1[nums1_end]
                nums1_end -= 1
