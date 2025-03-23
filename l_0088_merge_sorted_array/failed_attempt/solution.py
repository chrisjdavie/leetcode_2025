from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        i_nums1: int = 0
        i_nums2: int = 0

        # i_nums_tmp >= m + n?
        i_nums1_tmp: int = m

        max_num: int = 10**9

        print(" ", i_nums1, i_nums2, i_nums1_tmp, nums1)

        for i_cur in range(m + n):

            if nums1[i_nums1] <= nums2[i_nums2]:
                nums1[i_cur], nums1[i_nums1] = nums1[i_nums1], nums1[i_cur]
                i_nums1 +=1
            else:
                nums1[i_nums1_tmp] = nums1[i_cur]
                i_nums1 = i_nums1_tmp
                i_nums1_tmp += 1

                nums1[i_cur] = nums2[i_nums2]
                i_nums2 += 1

            print(i_cur, i_nums1, i_nums2, i_nums1_tmp, nums1)

            if i_nums1 == i_nums1_tmp or i_nums2 == n:
                print(i_nums1 == i_nums1_tmp, i_nums2 == n)
                break

        if m == 0:
            i_cur = -1

        # when i_nums2 is not depleted
        for i_nums2, i_cur_after in zip(range(i_nums2, n), range(i_cur + 1, n+m)):
            nums1[i_cur_after] = nums2[i_nums2]

        # when i_nums1 is not depleted
        for j, i_cur_after in enumerate(range(i_cur + 1, n+m)):
            i_nums1_tmp = m + j%n
            if i_nums1_tmp < i_cur_after:
                break
            nums1[i_cur_after], nums1[i_nums1_tmp] = nums1[i_nums1_tmp], nums1[i_cur_after]
            print(i_cur_after, i_nums1_tmp, nums1)
