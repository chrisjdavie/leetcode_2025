from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i_nums1_largest = m - 1
        j_nums1_largest = n - 1

        for k in range(m + n - 1, -1, -1):
            if j_nums1_largest < 0:
                break
            if i_nums1_largest >= 0 and nums1[i_nums1_largest] > nums2[j_nums1_largest]:
                nums1[k] = nums1[i_nums1_largest]
                i_nums1_largest -= 1
            else:
                nums1[k] = nums2[j_nums1_largest]
                j_nums1_largest -= 1
