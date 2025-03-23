from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j_nums1_largest = m - 1
        k_nums2_largest = n - 1

        for i in range(m + n - 1, -1, -1):
            if k_nums2_largest < 0:
                nums1[i] = nums1[j_nums1_largest]
                j_nums1_largest -= 1
            elif j_nums1_largest < 0:
                nums1[i] = nums2[k_nums2_largest]
                k_nums2_largest -= 1
            elif nums1[j_nums1_largest] >= nums2[k_nums2_largest]:
                nums1[i] = nums1[j_nums1_largest]
                j_nums1_largest -= 1
            else:
                nums1[i] = nums2[k_nums2_largest]
                k_nums2_largest -= 1
