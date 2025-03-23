from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        j: int = 0
        k: int = 0
        s: int = m

        print(nums1, " ", j, k, s)
        for i in range(m + n):
            if nums1[j] < nums2[k]:
                nums1[i], nums1[j] = nums1[j], nums1[i]
                j += 1
            else:
                nums1[s] = nums1[i]
                s += 1
                nums1[i] = nums2[k]
                k += 1
            if j > m:
                break
            print(nums1, i, j, k, s)

        print(nums1, i, j, k, s)

        for i1 in range(i, m + n):
            nums1[i1] = nums2[k]
            k += 1

        # j1: int = j
        # k: int = 0

        # for i1 in range(i+1, m + n):
        #     if j1 == n or k == j1:
        #         break
        #     if nums2[k] < nums2[j1]:
        #         nums1[i1] = nums2[k]
        #         k += 1
        #     else:
        #         nums1[i1] = nums2[j1]
        #         j1 += 1

        # if k < j:
        #     for d_k, i2 in enumerate(range(i1, m + n)):
        #         nums1[i2] = nums2[k + d_k]
        # else:
        #     for d_j, i2 in enumerate(range(i1, m+n)):
        #         nums1[i2] = nums2[j+d_j]

        # k = 0
        
        # for i in range(m+1, n):
        #     pass
