from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end_nums1: int = m - 1
        end_nums2: int = n - 1

        for end_merged in range(len(nums1) - 1, -1, -1):
            if end_nums2 < 0:
                break

            if end_nums1 < 0 or nums1[end_nums1] < nums2[end_nums2]:
                nums1[end_merged] = nums2[end_nums2]
                end_nums2 -= 1
            else:
                nums1[end_merged] = nums1[end_nums1]
                end_nums1 -= 1
